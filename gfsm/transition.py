'''
  The transition object has method: execute(). This method is called by a State
  when an event is dispatched that triggers the transition
'''
class Transition():
  def __init__(self, name, target, action):
    self.name = name
    self.target = target
    self.action = action
    self.start_action = None
    self.end_action = None

  def set_start_action(self, action):
    self.start_action = action

  def set_end_action(self, action):
    self.end_action = action

  def execute(self, context):
    if self.start_action is not None:
      self.start_action(context)
    if self.action is not None:
      self.action(context)
    if self.end_action is not None:
      self.end_action(context)
    context.set_current_state(self.target)
