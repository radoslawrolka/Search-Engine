import numpy as np
import scipy.sparse as sparse
import os
import json


def initialize_matrix(config):
    def idf(word):
        return np.log(config['MAX_PAGES'] / word_in_diff_file[word])
    
    with open('./data/main_dict.json', 'r') as f:
        main_dict = json.load(f)
    with open('./data/words_in_diff_file.json', 'r') as f:
        word_in_diff_file = json.load(f)

    list_of_articles = []
    list_of_words = list(main_dict.keys())
    matrix = sparse.csc_matrix((0,0), dtype=np.float64)
    for file in os.listdir('./data/dicts'):
        list_of_articles.append(file[:-5])
        with open(f'./data/dicts/{file}', 'r') as f:
            local_dict = json.load(f)
            local_dict = {word: local_dict[word] * idf(word) for word in local_dict if word in main_dict}
            column = [local_dict[word] if word in local_dict else 0 for word in list_of_words]
            column = column / np.linalg.norm(column)
            matrix = sparse.hstack([matrix, sparse.csc_matrix(column).transpose()]).tocsc()

    with open('./data/list_of_articles.txt', 'w') as f:
        f.write('\n'.join(list_of_articles))
    with open('./data/list_of_words.txt', 'w') as f:
        f.write('\n'.join(list_of_words))
    sparse.save_npz('./data/matrix.npz', matrix)
            
