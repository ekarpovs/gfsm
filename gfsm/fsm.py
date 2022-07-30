'''
  This class is a central point of access to the FSM.
'''

from typing import Dict, List
from gfsm.context import Context

from gfsm.fsm_builder.fsm_builder import FsmBuilder
from gfsm.state import State


class FSM():
  def __init__(self, fsm_builder: FsmBuilder):
    fsm_builder.build()
    self._events: List[str] = fsm_builder.events
    self._states: Dict[str, State] = fsm_builder.states
    self._init_action = fsm_builder.init_action

  @property
  def events(self) -> List[str]:
    return self._events

  @property
  def states(self) -> Dict[str, State]:
    return self._states

  @property
  def state_names(self):
    return list(self._states.keys())

  @property
  def number_of_states(self) -> int:
    return len(self._states)

  @property
  def init_action(self):
    return self._init_action

  def start(self) -> None:
    if self._init_action is not None:
      self._init_action()
    return

  def dispatch(self, event_name, context: Context):
    # get current state by name
    current_state = self._states.get(context.current_state_name)
    current_state.dispatch(context, event_name)
    return
