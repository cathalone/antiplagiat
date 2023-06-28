import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import torch


def read_files(filename1, filename2, split):
	with open(filename1, encoding='utf-8') as f1, open(filename2, encoding='utf-8') as f2:
		if split:
			f1_data = f1.readlines()
			f2_data = f2.readlines()
		else:
			f1_data = f1.read()
			f2_data = f2.read()
		f1.close()
		f2.close()
		return f1_data, f2_data


def compute_cosine_similarity(text1, text2):
	# stores text in a list
	list_text = [text1, text2]

	# converts text into vectors with the TF-IDF
	vectorizer = TfidfVectorizer(stop_words='english')
	vectorizer.fit_transform(list_text)
	tfidf_text1, tfidf_text2 = vectorizer.transform([list_text[0]]), vectorizer.transform([list_text[1]])

	# computes the cosine similarity
	cs_score = cosine_similarity(tfidf_text1, tfidf_text2)

	return np.round(cs_score[0][0], 2)


if __name__ == '__main__':
	f = read_files('test2.py', 'test1.py', split=False)
	tokens1 = set(nltk.tokenize.word_tokenize(f[0]))
	tokens2 = set(nltk.tokenize.word_tokenize(f[1]))
	vectorizer = TfidfVectorizer(stop_words='english')
	vector1 = vectorizer.fit_transform(tokens1)
	vector2 = vectorizer.transform(tokens2)
	print(compute_cosine_similarity(f[0], f[1]))
