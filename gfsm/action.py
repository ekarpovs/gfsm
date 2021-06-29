
# Default user action's wrapper
def fsm_action(implementation):
  def execute(context):
    __name__ = implementation.__name__
    print("default wrapper for action:", __name__)
    # Separate user functions from a FSM

    # Get a relevant user data
    data = {}
    data = implementation(data)

    return context

  return execute
