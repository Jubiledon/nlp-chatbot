# Returns the user's name if known, otherwise a fallback.
def get_user_name(context, fallback="You"):
    return context.user_name if context.user_name != None else fallback
