# -*- coding: utf-8 -*-

import os
import datetime
from flask import *
from werkzeug import secure_filename
from server import app
from settings import ALLOWED_EXTENSIONS
from facebook_bot import fbBot

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/report/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # POST : 전송
        name = request.form['name']
        photo = request.files['file']
        quality = request.form['quality']
        cost = request.form['cost']
        comment = request.form['comment']

        message = ''
        message += name + '\n'
        message += u'퀄리티 : '
        for i in range(0, int(quality)):
            message += u'★'
        message += '\n'
        message += u'가성비 : '
        for i in range(0, int(cost)):
            message += u'★'
        message += '\n'
        message += u'코멘트 : ' + comment
        message = message.encode('utf-8')

        filename = None
        if photo and allowed_file(photo.filename):
            now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_")
            filename = secure_filename(now + photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        fbBot.post(message, filename)
        return render_template('report.html', submit = True)
    elif request.method == 'GET':
        # GET : 입력폼 보이기
        return render_template('report.html', submit = False)
