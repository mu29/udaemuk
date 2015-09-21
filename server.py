#-*- coding: utf-8 -*-

from flask import *
from settings import MODULES

app = Flask(__name__)

app.secret_key = 'secretkey'

@app.route('/')
def index():
    return ""

def init_server():
    for module in MODULES:
        __import__(module)
