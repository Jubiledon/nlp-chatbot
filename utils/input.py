def get_user_input(prompt, context):
    raw = input(prompt)
    name = context.get_user_name() if context.has_user_name() else "You"
    print(f"{name}: {raw}")
    return raw
