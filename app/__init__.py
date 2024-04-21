import json
from flask import Flask

app = Flask(__name__)
with open('config.json') as f:
    config = json.load(f)

app.config.update(config)

from app import routes
