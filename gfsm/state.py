'''
  This class models the states in the FSM. Each State has a name that can be set as a property
  in this class. State also provides a method to associate events with transitions. It also provides a
  dispatch method to trigger transitions for incoming events. The dispatch method (after finding the
  right transition) first executes the state-exit action. Subsequently the transition is executed and then
  the target State in the transition is set as the current State in the context. Finally the state-entry
  method for the target State is executed
'''
class State():
  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.entry_action = None
    self.exit_action = None
    self.transitions = dict()

  def set_entry_action(self, action):
    self.entry_action = action

  def get_entry_action(self):
    return self.entry_action

  def set_exit_action(self, action):
    self.exit_action = action

  # the method to associate events with transitions.
  def add_transition(self, event_name, transition):
    self.transitions[event_name] = transition

  def dispatch(self, context, event_name):
    if event_name in self.transitions:
      if self.exit_action is not None:
        self.exit_action(context)
      tr = self.transitions[event_name]
      print("src {} dispatch event {} - Transition {} to {}".format(self.name, event_name, tr.name, tr.target.name))
      self.transitions[event_name].execute(context)
    else:
      print("src {} dispatch event {} - stay at the state".format(self.name, event_name))
