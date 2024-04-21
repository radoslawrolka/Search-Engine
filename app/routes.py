from app import app
from flask import render_template, redirect, url_for, json

"""
cosine_query_search(query, matrix, list_of_articles, list_of_words)
svd_lowrank_query_search(query, list_of_articles, list_of_words, k=5)
"""

@app.route('/cosine')
def cosine():
    