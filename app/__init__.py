import json
from flask import Flask
from scipy import sparse

app = Flask(__name__)
with open('config.json', encoding='utf-8') as f:
    config = json.load(f)

app.config.update(config)
"""
app.config['MATRIX'] = sparse.load_npz('./data/matrix.npz')
with open('./data/list_of_articles.txt', 'r') as f:
    app.config['LIST_OF_ARTICLES'] = f.read().split('\n')
with open('.data/list_of_words.txt', 'r') as f:
    app.config['LIST_OF_WORDS'] = f.read().split('\n')
"""
from app import routes
