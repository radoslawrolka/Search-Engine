import json
from flask import Flask
from scipy import sparse
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
with open('config.json', encoding='utf-8') as f:
    config = json.load(f)

app.config.update(config)
app.config['MATRIX'] = sparse.load_npz('./data/matrix.npz')
for k in [50, 100, 200]:
    with open(f'./data/svd_{k}/U.npy', 'rb') as f:
        U = np.load(f)
    with open(f'./data/svd_{k}/s.npy', 'rb') as f:
        s = np.load(f)
    with open(f'./data/svd_{k}/V.npy', 'rb') as f:
        V = np.load(f)
    app.config[f'SVD_{k}'] = [U, s, V]
with open('./data/list_of_articles.txt', 'r', encoding='utf-8') as f:
    app.config['LIST_OF_ARTICLES'] = f.read().split('\n')
with open('./data/list_of_words.txt', 'r', encoding='utf-8') as f:
    app.config['LIST_OF_WORDS'] = f.read().split('\n')

from app import routes
