
# Default user action's wrapper
def fsm_action(implementation):
  def execute(context):
    __name__ = implementation.__name__
    print("default wrapper for action:", __name__)
    # Separate user functions from a FSM

    # Get a relevant user data
    key = "user_data"
    data = context.get(key)
    # current_state = context.get_current_state()
    # if current_state:
    #   print("current state", current_state)

    data = implementation(data)

    # Store the new user data
    print("context", context.name)
    context.put(key, data)


    return context

  return execute
