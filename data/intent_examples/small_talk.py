INTENT_EXAMPLES = [
    # greetings
    ("hi", "small_talk", "greet"),
    ("hello", "small_talk", "greet"),
    ("hey", "small_talk", "greet"),
    ("yo", "small_talk", "greet"),
    ("good morning", "small_talk", "greet"),
    ("good evening", "small_talk", "greet"),

    # asking wellbeing
    ("how are you", "small_talk", "ask_wellbeing"),
    ("how's it going", "small_talk", "ask_wellbeing"),
    ("how are things", "small_talk", "ask_wellbeing"),

    # responding positively
    ("i'm good", "small_talk", "user_wellbeing_positive"),
    ("i'm great", "small_talk", "user_wellbeing_positive"),
    ("doing well", "small_talk", "user_wellbeing_positive"),
    ("all good", "small_talk", "user_wellbeing_positive"),

    # responding negatively / neutral
    ("not great", "small_talk", "user_wellbeing_negative"),
    ("i'm tired", "small_talk", "user_wellbeing_negative"),
    ("could be better", "small_talk", "user_wellbeing_negative"),

    # politeness
    ("nice to meet you", "small_talk", "polite_response"),
    ("nice meeting you", "small_talk", "polite_response"),

    # casual chat
    ("whats up", "small_talk", "casual"),
    ("what's new", "small_talk", "casual"),
]
