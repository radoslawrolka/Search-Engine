import data_getter.web_crawler as web_crawler
import json


with open('./config.json') as f:
    config = json.load(f)