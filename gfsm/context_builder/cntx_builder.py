import operation_loader
from ..context import Context
from ..action import fsm_action

class ContextBuilder():
  def __init__(self):
    pass
  
  def build(self, config, fsm):
    print("FSM context bulder. Build the {}".format(config['info']))
    context = Context(config['name'])
    # set the context init action
    init_action_name = config['first-state']['init-action']
    action_wrapper = fsm.get_fsm_action_wrapper()
    init_action = operation_loader.get(init_action_name)
    init_action = action_wrapper(init_action)
    context.set_init_action(init_action)

    # set init state 
    first_state_name = config['first-state']['name']
    states = fsm.get_impl()['states']
    for state in states:
      if states[state].name == first_state_name:
        context.set_current_state(states[state])

    return context
