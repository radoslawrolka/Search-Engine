import numpy as np

def search(query_vector, matrix, k):
    query_vector = query_vector / np.linalg.norm(query_vector)
    result = query_vector @ matrix
    articles_idx = np.argpartition(result, result.size - k)[-k:]
    return zip(articles_idx[np.argsort(result[articles_idx])][::-1], result[articles_idx[np.argsort(result[articles_idx])][::-1]])
