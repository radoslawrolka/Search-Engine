import data_getter.web_crawler as web_crawler
import data_process.text_processing as text_processing
import data_process.matrix_creation as matrix_creation
import engine.cosine as cosine_search
import engine.svd as svd_search
import engine.query as query_processing
import numpy as np
import json
import os
import scipy.sparse as sparse

with open('./config.json') as f:
    config = json.load(f)

# documents = web_crawler.get_data(config)
# text_processing.text_preprocessing(config)

# matrix_creation.initialize_matrix(config)
matrix = sparse.load_npz('./data/matrix.npz')

# matrix_creation.initialize_svd(matrix, 5)
svd_dict = {5: [np.load('./data/svd_5/U.npy'),
                   np.load('./data/svd_5/s.npy'),
                   np.load('./data/svd_5/V.npy')]}

list_of_articles = []
with open('./data/list_of_articles.txt', 'r') as f:
    list_of_articles = f.read().split('\n')
list_of_articles = list(filter(None, list_of_articles))
list_of_words = []
with open('./data/list_of_words.txt', 'r') as f:
    list_of_words = f.read().split('\n')
list_of_words = list(filter(None, list_of_words))

query = 'Christopher Nolan'

def cosine_query_search(query, matrix, list_of_articles, list_of_words, results_num=10):
    processed_query = query_processing.process_query(query)
    vector = query_processing.to_vector(processed_query, list_of_words)
    result = cosine_search.search(vector, matrix, results_num)
    for name, perc in result:
        print(list_of_articles[name], perc)
    return result

def svd_lowrank_query_search(query, list_of_articles, list_of_words, results_num=10, k=1000):
    if k not in svd_dict:
        return 'SVD matrix not loaded'
    else:
        U, s, V = svd_dict[k]
        processed_query = query_processing.process_query(query)
        vector = query_processing.to_vector(processed_query, list_of_words)
        result = svd_search.search(vector, U, s, V, results_num, k)
        for name, perc in result:
            print(list_of_articles[name], perc)
        return result

cosine_query_search(query, matrix, list_of_articles, list_of_words)
svd_lowrank_query_search(query, list_of_articles, list_of_words, k=5)