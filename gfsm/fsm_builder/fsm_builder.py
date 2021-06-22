import operation_loader
import sys

from gfsm.transition import Transition
from gfsm.event import Event
from gfsm.state import State
from ..action import fsm_action

class FsmBuilder():
  def __init__(self, config):
    self.config = config
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


  def build(self):
    self.set_runtime_environment()
    print("FSM bulder. Build the {}".format(self.config['info']))
    fsm_implementation = {}

    states_def = self.config['states']
    states = {}
    for state_def in states_def:
      print("State", state_def)
      state = self.build_state(state_def)
      states[state.name] = state

    print("Created States", states)

    cfg_events = self.config['events']
    events = {}
    for en in cfg_events:
      print("Event", en)
      events[en] = Event(en)
    print("Created Events", events)  


    cfg_transitions = self.config['transitions']
    transitions = {}
    for trdef in cfg_transitions:
      print("Transition", trdef)
      tr_name = trdef['name']
      tr_event = trdef['event']
      src = states[trdef['src']]
      target = states[trdef['target']] 
      tr_action = None
      action = None
      if 'action' in trdef:
        tr_action = trdef['action'] # Load the action from actions implementation by name
        action = self.action_wrapper(operation_loader.get(tr_action))
        print("action", action)
      transition = Transition(tr_name, target, action)
      transitions[tr_name] = transition
      # event = Event(tr_event)
      print("Associate event with Transition via State")
      src.add_transition(tr_event, transition)
    print("Created Transitions", transitions)  

    fsm_implementation['first-state'] = states[self.config['first-state']]
    fsm_implementation['action-wrapper'] = self.action_wrapper
    fsm_implementation['events'] = events
    fsm_implementation['states'] = states
    fsm_implementation['transitions'] = transitions

    return fsm_implementation
