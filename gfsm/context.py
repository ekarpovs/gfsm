'''
  This class maintains a reference to the current State (is generally changed by executing transitions)
  and functions as an object repository for actions. Actions can store objects in the
  context using the put method. The objects can later be retrieved using the get method. 
  Whenever a new FSMContext object is created (FSM instantiation), the init action is executed. 
  This action can be used to pre-define variables for the actions in the FSM.
'''

from typing import Dict


class Context():
  def __init__(self, name: str='test context'):
    self._name = name
    self._data_repo = dict()
    self._current_state_name: str = ''
    self._init_action = None

  @property
  def init_action(self):
    return self._init_action

  @init_action.setter
  def init_action(self, action):
    self._init_action = action
    return

  @property
  def current_state_name(self) -> str:
    return self._current_state_name

  @current_state_name.setter
  def current_state_name(self, state_name) -> None:
    self._current_state_name = state_name
    return

  # store restore user data
  def get_user_data(self, key: str) -> Dict:
    return self._data_repo.get(key)

  def set_user_data(self, key: str, data: Dict) -> None:
    self._data_repo[key] = data
    return
  
