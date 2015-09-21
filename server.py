#-*- coding: utf-8 -*-

from flask import *
from load_modules import MODULE_NAMES

app = Flask(__name__)

app.secret_key = 'secretkey'

@app.route('/')
def index():
    return ""

def init_server():
    for module_name in MODULE_NAMES:
        __import__(module_name)
