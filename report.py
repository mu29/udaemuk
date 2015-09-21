# -*- coding: utf-8 -*-

import os
from flask import *
from werkzeug import secure_filename
from server import app
from settings import ALLOWED_EXTENSIONS

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/report/', methods=['POST', 'GET'])
def login():
    # POST : 전송
    if request.method == 'POST':
        file = request.files['file']
        print file.filename
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print app.config['UPLOAD_FOLDER']
        return ""
    elif request.method == 'GET':
        # GET : 입력폼 보이기
        return render_template('report.html')
