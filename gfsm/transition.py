'''
  The transition object has method: execute(). This method is called by a State
  when an event is dispatched that triggers the transition
'''
class Transition():
  def __init__(self, name, target, action):
    self.name = name
    self.target = target
    self.action = action
    self.action_before = None
    self.action_after = None

  def process(self):
    pass

  
  def set_action_before(self, action):
    self.action_before = action

  def set_action_after(self, action):
    self.action_after = action

  def execute(self, context):
    if self.action is not None:
      self.action(context)
    context.set_current_state(self.target)