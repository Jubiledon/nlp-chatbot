import re

def handle_identity(text, user_name):
    if "my name is" in text.lower():
        name = re.sub(r".*my name is ", "", text.lower()).strip().capitalize()
        print(f"Nice to meet you, {name}!")
        return name
    elif "what is my name" in text.lower():
        if user_name:
            print(f"Your name is {user_name}.")
        else:
            print("I don’t know your name yet.")
        return user_name
    else:
        print("Could you tell me your name?")
        return user_name