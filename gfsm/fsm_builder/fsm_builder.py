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

  def set_runtime_environment(self):
    user_actions_path = self.config['user-actions-path']
    sys.path.append(user_actions_path)
    user_action_wrapper_path = self.config['user-action-wrapper-path']
    if len(user_action_wrapper_path) > 1:
      sys.path.append(user_action_wrapper_path)
    user_action_wrapper_name = self.config['user-action-wrapper-name']
    if len(user_action_wrapper_name) > 3 and '.' in user_action_wrapper_name :
      self.action_wrapper = operation_loader.get(user_action_wrapper_name)

  def build(self):
    self.set_runtime_environment()
    print("FSM bulder. Build the {}".format(self.config['info']))
    fsm_implementation = {}

    cfg_states = self.config['states']
    states = {}
    for sn in cfg_states:
      print("State", sn)
      states[sn] = State(sn)

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
      event = Event(tr_event)
      print("Associate event with Transition via State")
      src.add_transition(event, transition)
    print("Created Transitions", transitions)  

    fsm_implementation['action-wrapper'] = self.action_wrapper
    fsm_implementation['events'] = events
    fsm_implementation['states'] = states
    fsm_implementation['transitions'] = transitions

    return fsm_implementation
