# User actions implementation

# Test user action's wrapper example
def fsm_action(implementation):
  def execute(context):
    __name__ = implementation.__name__
    print("test wrapper for action:", __name__)
    # Separate user functions from a FSM

    # Get a relevant user datacls
    data = {}

    data = implementation(data)

    return context

  return execute

def init_context(data):
  # Do thomething
  return data

def entry_start(data):
  # Do thomething
  return data

def exit_start(data):
  # Do thomething
  return data

def entry_1(data):
  # Do thomething
  return data

def exit_1(data):
  # Do thomething
  return data

def entry_2(data):
  # Do thomething
  return data

def exit_2(data):
  # Do thomething
  return data

def entry_3(data):
  # Do thomething
  return data

def exit_3(data):
  # Do thomething
  return data

def entry_end(data):
  # Do thomething
  return data

def exit_end(data):
  # Do thomething
  return data

def action_1(data):
  # Do thomething
  return data

def action_2(data):
  # Do thomething
  return data

def action_3(data):
  # Do thomething
  return data

def action_4(data):
  # Do thomething
  return data

def start_transition(context):
  return context

def end_transition(context):
  return context