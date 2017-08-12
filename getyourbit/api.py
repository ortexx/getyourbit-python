"""Getyourbit.com client"""

import re
import json
import requests

class Api:
    def __init__(self, url):
        self.url = re.sub(r'[\/]+$', '', url)
        self.token = None

    def __request(self, url, **kwargs):
        response = requests.post(url, **kwargs)
        body = response.json() 

        if 'error' in body:
            message = body['message']
            if 'meta' in body:
                message += ' ' + json.dumps(body['meta'])
            raise Exception(message)

        return body

    def __next(self, res, url, scroll, callback, **kwargs):
        if scroll:
            kwargs['json']['scroll'] = scroll    

        body = self.request(url, **kwargs)
        res += body['data']  

        if callback:
            callback(body, body['data'], res)

        if('scroll' in body and body['scroll']):
            return self.__next(res, url, body['scroll'], callback, **kwargs)

        return res

    def auth(self, user, password, **kwargs):
        kwargs['auth'] = (user, password)
        body = self.__request(self.url + '/auth/', **kwargs)
        self.token = body['token']   

        return self.token

    def logout(self, **kwargs):
        if not self.token:
            raise Exception('You have to login before to logout')

        kwargs['json'] = {'token': self.token}
        body = self.__request(self.url + '/logout/', **kwargs)  
        self.token = None

        return body

    def request(self, url, data={}, **kwargs):       
        if 'json' in kwargs:
            data = kwargs['json'] 

        if 'data' in kwargs:
            data = kwargs['data']

        kwargs['json'] = data
        kwargs['json']['token'] = self.token   
        url = self.url + '/' + re.sub(r'^[\/]+', '', url) 

        return self.__request(url, **kwargs)

    def scroll(self, url, data={}, callback=None, **kwargs):
        if 'json' in kwargs:
            data = kwargs['json']
        kwargs['json'] = data
        res = []
        
        return self.__next(res, url, None, callback, **kwargs)   