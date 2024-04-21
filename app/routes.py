from app import app
from flask import json, request, jsonify
import data_process.text_processing as text_processing
import data_process.matrix_creation as matrix_creation
import engine.cosine as cosine_search
import engine.svd as svd_search
import engine.query as query_processing
import sys
sys.path.append('..')

@app.route('/cosine', methods=['GET'])
def cosine():
    query_param = request.args.get('query', default = '', type = str)
    results_num = request.args.get('results_num', default = 10, type = int)
    processed_query = query_processing.process_query(query_param)
    vector = query_processing.to_vector(processed_query, app.config['LIST_OF_WORDS'])
    result = cosine_search.search(vector, app.config['MATRIX'], results_num)
    return jsonify({'result': result}), 200

@app.route('/svd', methods=['GET'])
def svd():
    query_param = request.args.get('query', default = '', type = str)
    results_num = request.args.get('results_num', default = 10, type = int)
    k_param = request.args.get('k', default = 1000, type = int)
    U, s, V = app.config['SVD_DICT'][k_param]
    processed_query = query_processing.process_query(query_param)
    vector = query_processing.to_vector(processed_query, app.config['LIST_OF_WORDS'])
    result = svd_search.search(vector, U, s, V, results_num)
    return jsonify({'result': result}), 200