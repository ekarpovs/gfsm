import operation_loader
import sys

from gfsm.transition import Transition
from gfsm.event import Event
from gfsm.state import State
from ..action import fsm_action

class FsmBuilder():
  def __init__(self, config, definition):
    self.config = config
    self.definition = definition
    self.action_wrapper = fsm_action

  @staticmethod
  def is_correct_action_name(name):
    if name and name.strip() and len(name) >= 3 and '.' in name:
      return True
    return False

  @staticmethod
  def get_value(data, key):
    if key and key.strip() and key in data:
      return data[key]
    return ''

  def set_runtime_environment(self):
    user_actions_paths = self.get_value(self.config, 'user-actions-paths')
    for path in user_actions_paths:
      sys.path.append(path)
    user_action_wrapper_path = self.get_value(self.config, 'user-action-wrapper-path')
    if len(user_action_wrapper_path) > 1:
      sys.path.append(user_action_wrapper_path)
    user_action_wrapper_name = self.get_value(self.config, 'user-action-wrapper-name')
    if self.is_correct_action_name(user_action_wrapper_name):
      self.action_wrapper = operation_loader.get(user_action_wrapper_name)

  # Load the action from actions implementation by name
  def load_action(self, action_name):
    if self.is_correct_action_name(action_name):
      return self.action_wrapper(operation_loader.get(action_name))
    return None

  def build_state(self, state_def):
    name = self.get_value(state_def, 'name')
    entry_action = self.load_action(self.get_value(state_def, 'entry-action'))
    exit_action = self.load_action(self.get_value(state_def, 'exit-action'))
    state = State(name)
    state.set_entry_action(entry_action)
    state.set_exit_action(exit_action)     

    return state

  def build_transition(self, tr_def, states):
    tr_name = self.get_value(tr_def, 'name')
    tr_event = self.get_value(tr_def, 'event')
    target = states[self.get_value(tr_def, 'target')] 
    tr_action = self.get_value(tr_def, 'action')
    action = self.load_action(tr_action)
    transition = Transition(tr_name, target, action)
    # associate the event with Transition via State
    src = states[self.get_value(tr_def, 'src')]
    src.add_transition(tr_event, transition)

    return transition


  def build_transitions(self, trs_def, states):
    for tr_def in trs_def:
      self.build_transition(tr_def, states)
    return


  def build(self):
    self.set_runtime_environment()
    print("FSM bulder. Build the fsm implementation from: {}".format(self.config['info']))
    fsm_implementation = {}
    # build events
    events_def = self.config['events']
    events = {}
    for en in events_def:
      events[en] = Event(en)

    # build states
    states_def = self.get_value(self.definition,'states')
    states = {}
    for state_def in states_def:
      state = self.build_state(state_def)
      states[state.name] = state
    # build transitions and sssociate events with Transition via State"
    for state_def in states_def:
      trs_def = self.get_value(state_def, 'transitions')
      self.build_transitions(trs_def, states)

    # get init action
    init_action = self.load_action(self.get_value(self.definition, 'init-action'))

    # Setup FSM implementation
    fsm_implementation['init-action'] = init_action
    fsm_implementation['events'] = events
    fsm_implementation['first-state'] = states[self.get_value(self.definition, 'first-state')]
    fsm_implementation['states'] = states

    return fsm_implementation
