from app import app
from flask import json, request, jsonify
import data_process.text_processing as text_processing
import data_process.matrix_creation as matrix_creation
import engine.cosine as cosine_search
import engine.svd as svd_search
import engine.query as query_processing
import sys
sys.path.append('..')
import numpy as np

@app.route('/cosine', methods=['GET'])
def cosine():
    query_param = request.args.get('query', default = '', type = str)
    results_num = request.args.get('results_num', default = 10, type = int)
    processed_query = query_processing.process_query(query_param)
    vector = query_processing.to_vector(processed_query, app.config['LIST_OF_WORDS'])
    result = cosine_search.search(vector, app.config['MATRIX'], results_num)
    response = [[app.config['LIST_OF_ARTICLES'][name], round(100*(0 if np.isnan(perc) else perc), 2)] for name, perc in result]
    return jsonify({'result': response}), 200

@app.route('/svd_50', methods=['GET'])
def svd_50():
    query_param = request.args.get('query', default = '', type = str)
    results_num = request.args.get('results_num', default = 10, type = int)
    U, s, V = app.config['SVD_50']
    processed_query = query_processing.process_query(query_param)
    vector = query_processing.to_vector(processed_query, app.config['LIST_OF_WORDS'])
    result = svd_search.search(vector, U, s, V, results_num)
    response = [[app.config['LIST_OF_ARTICLES'][name], round(100*(0 if np.isnan(perc) else perc), 2)] for name, perc in result]
    return jsonify({'result': response}), 200

@app.route('/svd_100', methods=['GET'])
def svd_100():
    query_param = request.args.get('query', default = '', type = str)
    results_num = request.args.get('results_num', default = 10, type = int)
    U, s, V = app.config['SVD_100']
    processed_query = query_processing.process_query(query_param)
    vector = query_processing.to_vector(processed_query, app.config['LIST_OF_WORDS'])
    result = svd_search.search(vector, U, s, V, results_num)
    response = [[app.config['LIST_OF_ARTICLES'][name], round(100*(0 if np.isnan(perc) else perc), 2)] for name, perc in result]
    return jsonify({'result': response}), 200

@app.route('/svd_200', methods=['GET'])
def svd_200():
    query_param = request.args.get('query', default = '', type = str)
    results_num = request.args.get('results_num', default = 10, type = int)
    U, s, V = app.config['SVD_200']
    processed_query = query_processing.process_query(query_param)
    vector = query_processing.to_vector(processed_query, app.config['LIST_OF_WORDS'])
    result = svd_search.search(vector, U, s, V, results_num)
    response = [[app.config['LIST_OF_ARTICLES'][name], round(100*(0 if np.isnan(perc) else perc), 2)] for name, perc in result]
    return jsonify({'result': response}), 200
