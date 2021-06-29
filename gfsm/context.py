'''
  This class maintains a reference to the current State (is generally changed by executing transitions)
  and functions as an object repository for actions. Actions can store objects in the
  context using the put method. The objects can later be retrieved using the get method. 
  Whenever a new FSMContext object is created (FSM instantiation), the init action is executed. 
  This action can be used to pre-define variables for the actions in the FSM.
'''
class Context():
  def __init__(self, name):
    self.name = name
    #  an object repository for actions
    self.data_repo = dict()

    self.current_state = None
    # This action is used to pre-define variables for the actions in the FSM
    self.init_action = None

  def set_init_action(self, action):
    self.init_action = action

  def set_current_state(self, state):
    if self.current_state is None and self.init_action is not None:
      self.init_action(self)

    self.current_state = state
    entry_action = state.get_entry_action()
    if entry_action is not None:
      entry_action(self)

  
  def get_current_state_id(self):
    return self.current_state.id

  # store restore user data
  def put(self, key, data):
    self.data_repo[key] = data

  def get(self, key, default=None):
    if key in self.data_repo:
      return self.data_repo[key]
    return default

  # perform event
  def dispatch(self, event_name):
    print("current state", self.current_state.name)
    self.current_state.dispatch(self, event_name)
    print("new state", self.current_state.name)
  
