
# Default user action's wrapper
def fsm_action(implementation):
  def execute(context):
    __name__ = implementation.__name__
    print("default wrapper for action:", __name__)
    # Separate user functions from a FSM

    # Get a relevant user data
    key = "user_data"
    data = context.get(key)

    context = implementation(data)
    print("context", context.name)

    # Store the new user data
    context.put(key, data)


    return context

  return execute
