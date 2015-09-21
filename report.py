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
        print request.form
        name = request.form['name']
        photo = request.files['file']
        quality = request.form['quality']
        cost = request.form['cost']
        comment = request.form['comment']

        if photo and allowed_file(photo.filename):
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return ""
    elif request.method == 'GET':
        # GET : 입력폼 보이기
        return render_template('report.html')
