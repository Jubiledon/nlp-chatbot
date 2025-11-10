def handle_small_talk(text):
    if "how are you" in text.lower():
        return "I'm doing great, thanks for asking! How about you?"
    elif any(greet in text.lower() for greet in ["hi", "hello"]):
        return "Hi there! What’s your name?"
    else:
        return "Hey!"