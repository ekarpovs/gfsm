
# Decorator for an action
def fsm_action(implementation):
  def execute(context):
    __name__ = implementation.__name__
    print("action", __name__)

    context = implementation(context)
    print("context", context.name)

    return context

  return execute
