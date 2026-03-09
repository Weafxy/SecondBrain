from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def suggest_links(notes, new_note, threshold=0.2):
    """Gibt semantisch ähnliche Notizen zurück"""
    if not notes:
        return []

    texts = [n["title"] + " " + n["content"] for n in notes] + [new_note["title"] + " " + new_note["content"]]
    ids = [n["id"] for n in notes]

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)

    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]

    suggested_ids = [ids[i] for i, score in enumerate(cosine_sim) if score >= threshold]
    return suggested_ids