#-*- coding: utf-8 -*-

from flask import *
from settings import MODULES, UPLOAD_FOLDER

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return ""

def init_server():
    for module in MODULES:
        __import__(module)
