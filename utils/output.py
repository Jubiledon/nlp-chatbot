import builtins

def bot_print(*args, **kwargs):
    message = " ".join(str(a) for a in args)
    builtins._original_print(f"Bot: {message}", **kwargs)
