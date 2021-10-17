'''
  This class maintains a reference to the current State (is generally changed by executing transitions)
  and functions as an object repository for actions. Actions can store objects in the
  context using the put method. The objects can later be retrieved using the get method. 
  Whenever a new FSMContext object is created (FSM instantiation), the init action is executed. 
  This action can be used to pre-define variables for the actions in the FSM.
'''

from .state import State

class Context():
  def __init__(self, name):
    self._name = name
    self._data_repo = dict()
    self._current_state: State = None
    self._init_action = None

  @property
  def init_action(self):
    return self._init_action

  @init_action.setter
  def init_action(self, action):
    self._init_action = action
    return

  @property
  def current_state(self):
    return self._current_state

  @current_state.setter
  def current_state(self, state):
    if self.current_state is None and self.init_action is not None:
      self.init_action(self)
    self._current_state = state
    entry_action = self.current_state.entry_action
    if entry_action is not None:
      entry_action(self)
    return

  @property
  def current_state_id(self):
    return self.current_state.id
 
  @property
  def current_state_name(self):
    return self.current_state.name

  # store restore user data
  @property
  def user_data(self, key, data):
    return self._data_repo[key]

  @user_data.setter
  def user_data(self, key, data):
    self._data_repo[key] = data
    return

  # perform event
  def dispatch(self, event_name):
    print("current state", self.current_state.name)
    self.current_state.dispatch(self, event_name)
    print("new state", self.current_state.name)
    return
  
