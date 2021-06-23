'''
  This class maintains a reference to the current State (is generally changed by executing transitions)
  and functions as an object repository for actions. Actions can store objects in the
  context using the put method. The objects can later be retrieved using the get method. 
  Whenever a new FSMContext object is created (FSM instantiation), the init action is executed. 
  This action can be used to pre-define variables for the actions in the FSM.
'''
class Context():
  def __init__(self, name='default context'):
    self.name = name
    #  an object repository for actions
    self.data_repo = dict() # may be stack
    self.data_repo['user-data'] = dict()

    self.current_state = None
    self.init_action = None
    self.fsm_action_wrapper = None

  def set_fsm_action_wrapper(self, wrapper):
    self.fsm_action_wrapper = wrapper

  def get_fsm_action_wrapper(self):
    return self.fsm_action_wrapper

  def set_current_state(self, state):
    entry_action = state.get_entry_action()
    if entry_action is not None:
      entry_action(self)
    self.current_state = state
  
  def get_current_state(self):
    return self.current_state


  def set_init_action(self, action):
    self.init_action = action

  # This action is used to pre-define variables for the actions in the FSM
  def run_init_action(self):
    if self.init_action is not None:
      self.init_action()

  def put(self, key, data):
    self.data_repo[key] = data

  def get(self, key):
    if key in self.data_repo:
      return self.data_repo[key]
    return None

  def dispatch(self, event_name):
    print("current state", self.current_state.name)
    self.current_state.dispatch(self, event_name)
    print("new state", self.current_state.name)
  
