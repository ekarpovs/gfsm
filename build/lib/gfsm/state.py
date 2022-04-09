'''
  This class models the states in the FSM. Each State has a name that can be set as a property
  in this class. State also provides a method to associate events with transitions. It also provides a
  dispatch method to trigger transitions for incoming events. The dispatch method (after finding the
  right transition) first executes the state-exit action. Subsequently the transition is executed and then
  the target State in the transition is set as the current State in the context. Finally the state-entry
  method for the target State is executed
'''

from .transition import Transition 

class State():
  def __init__(self, id=0, name=''):
    self.id = id
    self.name = name
    self._entry_action = None
    self._exit_action = None
    self._transitions = dict()

  @property
  def id(self):
    return self._id

  @id.setter
  def id(self, id):
    self._id = id
    return

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, name):
    self._name = name
    return

  @property
  def entry_action(self):
    return self._entry_action

  @entry_action.setter
  def entry_action(self, action):
    self._entry_action = action
    return

  @property
  def exit_action(self):
    return self._exit_action

  @exit_action.setter
  def exit_action(self, action):
    self._exit_action = action
    return

  # property to associate event with transitions.
  @property
  def transitions(self):
    return self._transitions

  # @transitions.setter
  # def transition(self, even_name, transition: Transition):
  #   self.transitions[even_name] = transition
  #   return

  def dispatch(self, context, event_name):
    if event_name in self.transitions:
      if self.exit_action is not None:
        self.exit_action(context)
      tr = self.transitions[event_name]
      print("src {} dispatch event {} - Transition {} to {}".format(self.name, event_name, tr.name, tr.target.name))
      self.transitions[event_name].execute(context)
    else:
      print("src {} dispatch event {} - stay at the state".format(self.name, event_name))
    return