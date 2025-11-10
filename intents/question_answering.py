from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def handle_question_answering(text, questions, answers):
    vectorizer = TfidfVectorizer().fit(questions + [text])
    vectors = vectorizer.transform(questions + [text])
    sims = cosine_similarity(vectors[-1], vectors[:-1]).flatten()
    best_idx = sims.argmax()
    if sims[best_idx] < 0.2:
        return "I'm not sure about that one."
    return answers[best_idx]