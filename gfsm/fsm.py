from .context import Context

class FSM():
  def __init__(self, fsm_impl, cntx_name):
    # wrapper = fsm_impl['action-wrapper']
    first_state = fsm_impl['first-state']
    init_action = fsm_impl['init-action']
    self.context = Context(cntx_name)
    self.context.set_init_action(init_action)
    self.context.run_init_action()
    self.context.set_current_state(first_state)

  def dispatch(self, event_name):
    self.context.dispatch(event_name)
  