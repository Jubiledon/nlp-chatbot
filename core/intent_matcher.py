from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

intents = {
    "small_talk": ["hi", "hello", "how are you"],
    "discoverability": ["what can you do", "help", "how can you help"],
    "identity": ["my name is", "what is my name", "call me"],
    "question_answering": ["what is", "who is", "when was", "where is", "what are"]
}

def get_most_similar(text, corpus):
    vectorizer = TfidfVectorizer().fit(corpus + [text])
    vectors = vectorizer.transform(corpus + [text])
    sims = cosine_similarity(vectors[-1], vectors[:-1]).flatten()
    best_idx = sims.argmax()
    return best_idx, sims[best_idx]

def match_intent(user_input):
    all_patterns = [p for patterns in intents.values() for p in patterns]
    intent_names = [name for name, patterns in intents.items() for _ in patterns]
    best_idx, score = get_most_similar(user_input, all_patterns)
    return intent_names[best_idx]