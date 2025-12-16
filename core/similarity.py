from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#
# Finds the best matching text from a data object/dictionary(corpus) 
# for a given input text (query).
#
def find_best_match(query, corpus):
    vectorizer = TfidfVectorizer().fit(corpus + [query])
    vectors = vectorizer.transform(corpus + [query])

    similarities = cosine_similarity(
        vectors[-1], vectors[:-1]
    ).flatten()

    best_idx = similarities.argmax()
    best_score = similarities[best_idx]

    return best_idx, best_score
