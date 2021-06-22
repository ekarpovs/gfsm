from .event import Event
from .context import Context
from .state import State
from .transition import Transition

class FSM():
  def __init__(self, fsm_impl, cntx_name):
    first_state = fsm_impl['first-state']
    wrapper = fsm_impl['action-wrapper']
    self.context = Context(cntx_name)
    self.context.set_current_state(first_state)
    self.context.set_fsm_action_wrapper(wrapper)


  def dispatch(self, event_name):
    self.context.dispatch(event_name)
  