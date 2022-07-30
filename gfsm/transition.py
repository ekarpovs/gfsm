from typing import Callable
from gfsm.context import Context


class Transition():
  '''
    The transition object has method: execute().
    This method is called by a State
    when an event is dispatched that triggers the transition
  '''

  def __init__(self, name: str, target_name: str, action: Callable):
    self.name = name
    self._target_name = target_name
    self._action = action
    self._start_action: Callable = None
    self._end_action: Callable = None

  @property
  def target_name(self) -> str:
    return self._target_name

  @property
  def action(self) -> Callable:
    return self._action

  @property
  def start_action(self) -> Callable:
    return self._start_action

  @start_action.setter
  def start_action(self, action: Callable):
    self._start_action = action

  @property
  def end_action(self) -> Callable:
    return self._end_action

  @end_action.setter
  def end_action(self, action: Callable):
    self._end_action = action

  def execute(self, context: Context) -> None:
    if self.start_action is not None:
      self.start_action(context)
    if self.action is not None:
      self.action(context)
    if self.end_action is not None:
      self.end_action(context)
    context.current_state_name = self._target_name
    return
