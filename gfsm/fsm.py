'''
  This class is a central point of access to the FSM. 
'''

from typing import Dict, List

from gfsm.fsm_builder.fsm_builder import FsmBuilder
from .context import Context
from .state import State

class FSM():
  def __init__(self, fsm_builder: FsmBuilder):
    self._context = Context()
    self._fsm_impl = fsm_builder.build()
    self._events: List[str] = self._fsm_impl.get('events')
    self._states: Dict[str, State] = self._fsm_impl.get('states')
    self._context.current_state_name = self._fsm_impl.get('first-state').name

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

  def start(self) -> None:
    init_action = self._fsm_impl.get('init-action', None)
    first_state = self._fsm_impl.get('first-state', State())
    self.init_action = init_action
    self.current_state = first_state
    if self.init_action is not None:
      self.init_action(self._context)
    return

  def dispatch(self, event_name):
    # get current state name from the context
    current_state_name = self._context.current_state_name
    current_state = self._states.get(current_state_name)
    current_state.dispatch(self.context, event_name)
    return