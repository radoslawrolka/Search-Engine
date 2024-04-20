import data_getter.web_crawler as web_crawler
import data_process.text_processing as text_processing
import data_process.matrix_creation as matrix_creation
import engine.query as query_search
import engine.svd as svd_search
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

list_of_articles = []
with open('./data/list_of_articles.txt', 'r') as f:
    list_of_articles = f.read().split('\n')
list_of_articles = list(filter(None, list_of_articles))
list_of_words = []
with open('./data/list_of_words.txt', 'r') as f:
    list_of_words = f.read().split('\n')
list_of_words = list(filter(None, list_of_words))

query = 'Christopher Nolan'

result = query_search.search(query, matrix, list_of_articles, list_of_words)
for name, perc in result:
    print(list_of_articles[name], perc)