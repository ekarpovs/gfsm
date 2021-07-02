
# Default user action's wrapper
def fsm_action(implementation):
  def execute(context):
    __name__ = implementation.__name__
    print("default wrapper for action:", __name__)

    context = implementation(context)    

    return context

  return execute
