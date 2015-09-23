# -*- coding: utf-8 -*-

import os
import facebook
from server import app
from settings import *

class FacebookBot:

    def __init__(self):
        config = {
            'page_id'      : PAGE_ID,
            'access_token' : ACCESS_TOKEN
        }
        self.api = self.get_api(config)

    def get_api(self, config):
        graph = facebook.GraphAPI(config['access_token'])
        response = graph.get_object('me/accounts')
        page_access_token = None
        for page in response['data']:
            if page['id'] == config['page_id']:
                page_access_token = page['access_token']
        graph = facebook.GraphAPI(page_access_token)
        return graph

    def post(self, message, photo):
        if photo is None:
            self.api.put_wall_post(message)
        else:
            path = os.path.join(app.config['UPLOAD_FOLDER'], photo)
            self.api.put_photo(open(path), message)

fbBot = FacebookBot()
