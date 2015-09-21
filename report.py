# -*- coding: utf-8 -*-

from flask import *
from server import app

@app.route('/report/', methods=['POST', 'GET'])
def login():
    # POST : 전송
    if request.method == 'POST':
    elif request.method == 'GET':
        # GET : 입력폼 보이기
        return render_template('report.html')
