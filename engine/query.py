import re
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import porter

def process_query(text):
    text = text.lower()
    text = re.sub(r'[^a-z]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    words = text.split(' ')
    words = [word for word in words if word not in stopwords.words('english')]
    words = [porter.PorterStemmer().stem(word) for word in words]
    words = [word for word in words if len(word) >= 3]
    return words

def search(query, matrix, list_of_articles, list_of_words, k=5):
    words = process_query(query)
    query_vector = np.zeros(len(list_of_words))
    for word in words:
        if word in list_of_words:
            query_vector[list_of_words.index(word)] += 1
    query_vector = query_vector / np.linalg.norm(query_vector)
    result = query_vector @ matrix
    articles_idx = np.argpartition(result, result.size - k)[-k:]
    return zip(articles_idx[np.argsort(result[articles_idx])][::-1], result[articles_idx[np.argsort(result[articles_idx])][::-1]])

