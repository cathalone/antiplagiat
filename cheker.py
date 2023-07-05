from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np



def compute_cosine_similarity(text1, text2):
	list_text = [text1, text2]
	vectorizer = TfidfVectorizer()
	vectorizer.fit_transform(list_text)
	tfidf_text1, tfidf_text2 = vectorizer.transform([list_text[0]]), vectorizer.transform([list_text[1]])

	cs_score = cosine_similarity(tfidf_text1, tfidf_text2)

	return np.round(cs_score[0][0], 2)

