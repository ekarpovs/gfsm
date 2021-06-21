from .event import Event
from .context import Context
from .state import State
from .transition import Transition

class FSM():
  def __init__(self, implementation):
    self.implementation = implementation

  def get_impl(self):
    return self.implementation

  def get_fsm_action_wrapper(self):
    return self.implementation['action-wrapper']


  def dispatch(self, event_name, context):
    print("current state", context.get_current_state().name)
    event = self.implementation['events'][event_name]
    context.dispatch(event)
    print("new state", context.get_current_state().name)
  