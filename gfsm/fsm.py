from .context import Context

class FSM():
  def __init__(self, cntx_name):
    self.context = Context(cntx_name)

  def start(self, fsm_impl):
    init_action = fsm_impl.get('init-action', None)
    first_state = fsm_impl.get('first-state')

    self.context.init_action = init_action
    self.context.current_state = first_state
    return

  def dispatch(self, event_name):
    self.context.dispatch(event_name)
    return