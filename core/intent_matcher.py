from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data.intent_examples import INTENT_EXAMPLES
from core.similarity import find_best_match

intents = {
    "small_talk": ["hi", "hello", "how are you"],
    "discoverability": ["what can you do", "help", "how can you help"],
    "identity": ["my name is", "what is my name", "call me", "do you know my name"],
    "question_answering": ["what is", "who is", "when was", "where is", "what are"]
}

#
# Matches user input to the best intent based on predefined example phrases.
#
def match_intent_and_subintent(user_input):
    phrases = [p for p, _, _ in INTENT_EXAMPLES]
    labels = [(intent, sub) for _, intent, sub in INTENT_EXAMPLES]
    intent_index, score = find_best_match(user_input, phrases)
    intent, sub_intent = labels[intent_index]
    return intent, sub_intent, score
