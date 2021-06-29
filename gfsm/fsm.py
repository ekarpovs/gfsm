from .context import Context

class FSM():
  def __init__(self, cntx_name):
    self.context = Context(cntx_name)

  def start(self, fsm_impl):
    init_action = fsm_impl['init-action']
    first_state = fsm_impl['first-state']
    self.context.set_init_action(init_action)
    self.context.set_current_state(first_state)


  def dispatch(self, event_name):
    self.context.dispatch(event_name)
    return self.context.get_current_state_id()