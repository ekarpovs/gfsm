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
    self._fsm_impl: Dict = fsm_builder.build()
    self._events: List[str] = self._fsm_impl.get('events')
    self._states: Dict[str, State] = self._fsm_impl.get('states')
    self._context.current_state_name = self._fsm_impl.get('first-state').name

  @property
  def init_action(self):
    return self._context.init_action
  
  @init_action.setter
  def init_action(self, action):
    self._context.init_action = action

  @property
  def state_names(self):
    return list(self._states.keys())

  @property
  def number_of_states(self):
    return len(self._states)

  @property
  def current_state_id(self):
    current_state = self._states.get(self._context.current_state_name)
    return current_state.id

  @property
  def current_state_name(self):
    return self._context.current_state_name

  def get_user_data(self, key):
    return self._context.get_user_data(key)

  def set_user_data(self, key, data):
    self._context.set_user_data(key, data)
    return

  def start(self) -> None:
    init_action = self._fsm_impl.get('init-action', None)
    first_state = self._fsm_impl.get('first-state', State())
    self.init_action = init_action
    self._context.current_state_name = first_state.name
    if self.init_action is not None:
      self.init_action(self._context)
    return

  def dispatch(self, event_name):
    # get current state by name
    current_state = self._states.get(self._context.current_state_name)
    current_state.dispatch(self._context, event_name)
    return