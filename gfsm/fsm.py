from .event import Event
from .context import Context
from .state import State
from .transition import Transition

class FSM():
  def __init__(self, wrapper, cntx_name):
    self.context = Context(cntx_name)
    self.context.set_fsm_action_wrapper(wrapper)

  def get_context(self):
    return self.context

  def dispatch(self, event_name):
    self.context.dispatch(event_name)
  