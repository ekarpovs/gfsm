from gfsm import fsm_action

@fsm_action
def init_action(context):
  # Get a relevant user data
  key = "user_data"
  data = context.get(key)
  # Do initialiation

  # Store the user data
  context.put(key, data)

  return context


@fsm_action
def action1(context):
  # Get a relevant user data
  key = "user_data"
  data = context.get(key)
  # Do initialiation

  # Store the user data
  context.put(key, data)

  return context


@fsm_action
def action2(context):
  # Get a relevant user data
  key = "user_data"
  data = context.get(key)
  # Run step
  
  # Store the user data
  context.put(key, data)

  return context

@fsm_action
def action3(context):
  # Get a relevant user data
  key = "user_data"
  data = context.get(key)
  # Run step
  
  # Store the user data
  context.put(key, data)

  return context
