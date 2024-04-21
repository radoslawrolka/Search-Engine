import re
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

def process_query(text):
    text = text.lower()
    text = re.sub(r'[^a-z]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    words = text.split(' ')
    words = [word for word in words if word not in stopwords.words('english')]
    words = [PorterStemmer().stem(word) for word in words]
    words = [word for word in words if len(word) >= 3]
    return words

def to_vector(words, list_of_words):
    query_vector = np.zeros(len(list_of_words))
    for word in words:
        if word in list_of_words:
            query_vector[list_of_words.index(word)] += 1
    query_vector = query_vector / np.linalg.norm(query_vector)
    return query_vector