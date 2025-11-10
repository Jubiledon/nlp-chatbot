from core.intent_matcher import match_intent
from intents.small_talk import handle_small_talk
from intents.discoverability import handle_discoverability
from intents.identity import handle_identity
from intents.question_answering import handle_question_answering
from core.qa_loader import load_qa_dataset

def main():
    print("Hello! I'm your chatbot. Type 'exit' to quit.")
    questions, answers = load_qa_dataset("data/COMP3074-CW1-Dataset.csv")
    user_name = None

    while True:
        user_input = input("> ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        intent = match_intent(user_input)

        if intent == "small_talk":
            print(handle_small_talk(user_input))
        elif intent == "discoverability":
            print(handle_discoverability())
        elif intent == "identity":
            user_name = handle_identity(user_input, user_name)
        elif intent == "question_answering":
            print(f"Loaded {len(questions)} questions and {len(answers)} answers.")
            print(handle_question_answering(user_input, questions, answers))
        else:
            print("Sorry, I didn’t quite get that.")

if __name__ == "__main__":
    main()