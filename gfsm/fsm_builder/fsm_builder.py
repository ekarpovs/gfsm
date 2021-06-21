import operation_loader
import sys

from gfsm.transition import Transition
from gfsm.event import Event
from gfsm.state import State
from ..action import fsm_action

class FsmBuilder():
  def __init__(self, config):
    self.config = config

  def set_build_environment(self):
    user_actions_path = self.config['user-actions-path']
    sys.path.append(user_actions_path)

  def build(self):
    self.set_build_environment()

    fsm_implementation = {}

    fsm_config = self.config['fsm']
    print("FSM bulder. Build the {}".format(fsm_config['info']))

    cfg_states = fsm_config['states']
    states = {}
    for sn in cfg_states:
      print("State", sn)
      states[sn] = State(sn)

    print("Created States", states)

    cfg_events = fsm_config['events']
    events = {}
    for en in cfg_events:
      print("Event", en)
      events[en] = Event(en)
    print("Created Events", events)  


    cfg_transitions = fsm_config['transitions']
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
        action = fsm_action(operation_loader.get(tr_action))
        print("action", action)
      transition = Transition(tr_name, target, action)
      transitions[tr_name] = transition
      event = Event(tr_event)
      print("Associate event with Transition via State")
      src.add_transition(event, transition)
    print("Created Transitions", transitions)  

    fsm_implementation['events'] = events
    fsm_implementation['states'] = states
    fsm_implementation['transitions'] = transitions

    return fsm_implementation
