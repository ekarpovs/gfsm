from .event import Event
from .context import Context
from .state import State
from .transition import Transition

class FSM():
  def __init__(self, cntx_name, first_state, wrapper):
    self.context = Context(cntx_name)
    self.context.set_current_state(first_state)
    self.context.set_fsm_action_wrapper(wrapper)


  # def get_fsm_action_wrapper(self):
  #   return self.context.get_fsm_action_wrapper()


  def dispatch(self, event_name):
    self.context.dispatch(event_name)
  