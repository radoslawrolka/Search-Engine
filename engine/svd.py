import numpy as np

def search(query_vector, U, s, V, results_num):
    query_vector = query_vector / np.linalg.norm(query_vector)
    qA = ((query_vector@U)@np.diag(s))@V
    result = sorted(enumerate(qA), key=lambda x: x[1], reverse=True)
    return result[:results_num]
