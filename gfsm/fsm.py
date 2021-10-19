'''
  This class is a central point of access to the FSM. 
'''

from .context import Context
from .state import State

class FSM():
  def __init__(self, cntx_name):
    self._context = Context(cntx_name)

  @property
  def context(self):
    return self._context

  @property
  def init_action(self):
    return self._context.init_action
  
  @init_action.setter
  def init_action(self, action):
    self._context.init_action = action

  @property
  def current_state(self):
    return self._context.current_state
  
  @current_state.setter
  def current_state(self, state):
    self._context.current_state = state

  @property
  def current_state_id(self):
    return self._context.current_state.id

  @property
  def current_state_name(self):
    return self._context.current_state.name

  def get_user_data(self, key):
    return self.context.get_user_data(key)

  def set_user_data(self, key, data):
    self.context.set_user_data(key, data)
    return

  def start(self, fsm_impl):
    init_action = fsm_impl.get('init-action', None)
    first_state = fsm_impl.get('first-state', State())
    self.init_action = init_action
    self.current_state = first_state
    return

  def dispatch(self, event_name):
    self._context.dispatch(event_name)
    return