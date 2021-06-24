from .context import Context

class FSM():
  def __init__(self, fsm_impl, cntx_name, init_data={}):
    # wrapper = fsm_impl['action-wrapper']
    self.context = Context(cntx_name, init_data)
    init_action = fsm_impl['init-action']
    first_state = fsm_impl['first-state']
    self.context.set_init_action(init_action)
    self.context.set_current_state(first_state)

  def dispatch(self, event_name):
    self.context.dispatch(event_name)
  