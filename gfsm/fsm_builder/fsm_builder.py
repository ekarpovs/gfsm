from typing import Dict, List
import operation_loader
import sys

from gfsm.transition import Transition
from gfsm.state import State
from gfsm.action import fsm_action


class FsmBuilder():
  def __init__(self, config: Dict, definition: Dict):
    self._config = config
    self._definition = definition
    self._action_wrapper = fsm_action
    self._first_state_name = ''
    self._init_action = None
    self._events: List[str] = []
    self._states: Dict[str, State] = {}

# API
  @property
  def events(self) -> List[str]:
    return self._events

  @property
  def states(self) -> Dict[str, State]:
    return self._states

  @property
  def first_state_name(self) -> str:
    return self._first_state_name

  @property
  def init_action(self):
    return self._init_action

#
  @staticmethod
  def _is_correct_action_name(name: str) -> bool:
    if name and name.strip() and len(name) >= 3 and '.' in name:
      return True
    return False

  @staticmethod
  def get_value(data: Dict, key: str) -> List[str] | str:
    if key and key.strip() and key in data:
      return data[key]
    return ''

  def _set_runtime_environment(self) -> None:
    user_actions_paths = self.get_value(self._config, 'user-actions-paths')
    for path in user_actions_paths:
      sys.path.append(path)
    user_action_wrapper_path = \
        self.get_value(self._config, 'user-action-wrapper-path')
    if len(user_action_wrapper_path) > 1:
      sys.path.append(user_action_wrapper_path)
    user_action_wrapper_name = \
        self.get_value(self._config, 'user-action-wrapper-name')
    if self._is_correct_action_name(user_action_wrapper_name):
        self._action_wrapper = operation_loader.get(user_action_wrapper_name)

  def _load_action(self, action_name):
    # Load the action from actions implementation by name
    if self._is_correct_action_name(action_name):
      if action_name.startswith('____'):
        # use defsult action's wrapper
        action_name = action_name[4:]
        return fsm_action(operation_loader.get(action_name))
      return self._action_wrapper(operation_loader.get(action_name))
    return None

  def _build_state(self, state_def: Dict, idx: int) -> None:
    name = self.get_value(state_def, 'name')
    entry_action = self._load_action(self.get_value(state_def, 'entry-action'))
    exit_action = self._load_action(self.get_value(state_def, 'exit-action'))
    state = State(idx, name)
    state.entry_action = entry_action
    state.exit_action = exit_action
    self._states[state.name] = state
    return

  def _build_transition(self, tr_def: Dict) -> None:
    tr_name = self.get_value(tr_def, 'name')
    tr_event = self.get_value(tr_def, 'event')
    target = self._states[self.get_value(tr_def, 'target')]
    tr_action = self.get_value(tr_def, 'action')
    action = self._load_action(tr_action)
    transition = Transition(tr_name, target.name, action)
    if 'start-action' in tr_def:
      tr_start_action = self.get_value(tr_def, 'start-action')
      start_action = self._load_action(tr_start_action)
      transition.start_action = start_action
    if 'end-action' in tr_def:
      tr_end_action = self.get_value(tr_def, 'end-action')
      end_action = self._load_action(tr_end_action)
      transition.end_action = end_action

    # associate the event with Transition via State
    src = self._states.get(self.get_value(tr_def, 'src'))
    src.transitions[tr_event] = transition
    return

  def _build_state_transitions(self, state_def: Dict) -> None:
    trs_def = self.get_value(state_def, 'transitions')
    for tr_def in trs_def:
      self._build_transition(tr_def)
    return

  def build(self) -> None:
    self._set_runtime_environment()
    print("FSM bulder. Build the fsm from: {}".format(self._config['info']))
    # build events
    events_def = self._config['events']
    for en in events_def:
      self._events.append(en)

    # build states
    states_def = self.get_value(self._definition, 'states')
    for i, state_def in enumerate(states_def):
      self._build_state(state_def, i)

    # build transitions and sssociate events with Transition via State"
    for state_def in states_def:
      self._build_state_transitions(state_def)

    # get init action
    init_action = \
        self._load_action(self.get_value(self._definition, 'init-action'))

    # Setup FSM implementation
    self._init_action = init_action
    self._first_state_name = self.get_value(self._definition, 'first-state')
    return
