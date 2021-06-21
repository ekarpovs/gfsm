# User actions implementation

# Test user action's wrapper
def fsm_action(implementation):
  def execute(context):
    __name__ = implementation.__name__
    print("test wrapper for action:", __name__)
    # Separate user functions from a FSM

    # Get a relevant user data
    key = "user_data"
    data = context.get(key)

    data = implementation(data)

    # Store the new user data
    print("context", context.name)
    context.put(key, data)


    return context

  return execute

def init_action(data):
  # Do thomething
  return data


def action1(data):
  # Do thomething
  return data


def action2(data):
  # Do thomething
  return data

def action3(data):
  # Do thomething
  return data
