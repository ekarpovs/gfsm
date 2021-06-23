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
    if len(name) > 3 and '.' in name:
      return True
    return False
  
  def set_runtime_environment(self):
    user_actions_paths = self.config['user-actions-paths']
    for path in user_actions_paths:
      sys.path.append(path)
    user_action_wrapper_path = self.config['user-action-wrapper-path']
    if len(user_action_wrapper_path) > 1:
      sys.path.append(user_action_wrapper_path)
    user_action_wrapper_name = self.config['user-action-wrapper-name']
    if self.is_correct_action_name(user_action_wrapper_name):
      self.action_wrapper = operation_loader.get(user_action_wrapper_name)

  def build_state(self, state_def):
    name = state_def['name']
    entry_action = None
    exit_action = None
    entry_action_name = state_def['entry-action']
    if self.is_correct_action_name(entry_action_name):
      entry_action = self.action_wrapper(operation_loader.get(entry_action_name))
    exit_action_name = state_def['exit-action']
    if self.is_correct_action_name(exit_action_name):
      exit_action = self.action_wrapper(operation_loader.get(exit_action_name))
    state = State(name)
    state.set_entry_action(entry_action)
    state.set_exit_action(exit_action)     

    return state

  def build_transition(self, tr_def, states):
    tr_name = tr_def['name']
    tr_event = tr_def['event']
    src = states[tr_def['src']]
    target = states[tr_def['target']] 
    tr_action = None
    action = None
    if 'action' in tr_def:
      tr_action = tr_def['action'] # Load the action from actions implementation by name
      if self.is_correct_action_name(tr_action):
        action = self.action_wrapper(operation_loader.get(tr_action))
        # print("action", action)
    transition = Transition(tr_name, target, action)
    # print("Associate event with Transition via State")
    src.add_transition(tr_event, transition)

    return transition


  def build_transitions(self, trs_def, states):
    transitions = {}
    for tr_def in trs_def:
      # print("Transition", tr_def)
      transition = self.build_transition(tr_def, states)
    transitions[tr_def['name']] = transition

    return transitions


  def build(self):
    self.set_runtime_environment()
    print("FSM bulder. Build the fsm implementation from: {}".format(self.config['info']))
    fsm_implementation = {}
    # build events
    events_def = self.config['events']
    events = {}
    for en in events_def:
      # print("Event", en)
      events[en] = Event(en)
    # print("Created Events", events)  

    # build states
    states_def = self.definition['states']
    states = {}
    for state_def in states_def:
      # print("State", state_def)
      state = self.build_state(state_def)
      states[state.name] = state
    # print("Created States", states)
    # build transitions and sssociate events with Transition via State"
    for state_def in states_def:
      trs_def = state_def['transitions']
      transitions = self.build_transitions(trs_def, states)
    # Setup FSM implementation
    fsm_implementation['events'] = events
    fsm_implementation['action-wrapper'] = self.action_wrapper
    fsm_implementation['first-state'] = states[self.definition['first-state']]
    fsm_implementation['states'] = states
    fsm_implementation['transitions'] = transitions

    return fsm_implementation
