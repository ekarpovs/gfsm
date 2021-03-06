'''
  This class models the states in the FSM.
  Each State has a name that can be set as a property
  in this class. State also provides a method to associate events
  with transitions. It also provides a dispatch method to trigger
  transitions for incoming events. The dispatch method (after finding the
  right transition) first executes the state-exit action.
  Subsequently the transition is executed and then
  the target State in the transition is set as the current
  State in the context. Finally the state-entry
  method for the target State is executed
'''

from typing import Callable, Dict

from gfsm.context import Context
from gfsm.transition import Transition


class State():
  def __init__(self, id: int = 0, name: str = ''):
    self.id = id
    self.name = name
    self._entry_action = None
    self._exit_action = None
    self._transitions: Dict[str, Transition] = dict()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int) -> None:
    self._id = id
    return

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str) -> None:
    self._name = name
    return

  @property
  def entry_action(self) -> Callable:
    return self._entry_action

  @entry_action.setter
  def entry_action(self, action: Callable) -> None:
    self._entry_action = action
    return

  @property
  def exit_action(self) -> Callable:
    return self._exit_action

  @exit_action.setter
  def exit_action(self, action: Callable) -> None:
    self._exit_action = action
    return

  @property
  def transitions(self) -> Dict[str, Transition]:
    return self._transitions

  def dispatch(self, context: Context, event_name: str) -> None:
    if event_name in self.transitions:
      if self.exit_action is not None:
        self.exit_action(context)
      tr = self.transitions[event_name]
      print("src {} dispatch event {} - Transition {} to {}"
            .format(self.name, event_name, tr.name, tr.target_name))
      self.transitions[event_name].execute(context)
    else:
      print("src {} dispatch event {} - stay at the state"
            .format(self.name, event_name))
    return
