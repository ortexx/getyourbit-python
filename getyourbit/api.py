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
        response = response.json()        
        if 'error' in response:
            message = response['message']
            if 'meta' in response:
                message += ' ' + json.dumps(response['meta'])
            raise Exception(message)
        return response

    def __next(self, res, url, scroll, callback, **kwargs):
        if scroll:
            kwargs['json']['scroll'] = scroll    
        response = self.request(url, **kwargs)
        res += response['data']        
        if callback:
            callback(response, response['data'], res)
        if('scroll' in response and response['scroll']):
            return self.__next(res, url, response['scroll'], callback, **kwargs)
        return res

    def auth(self, user, password, **kwargs):
        kwargs['auth'] = (user, password)
        response = self.__request(self.url + '/auth/', **kwargs)
        self.token = response['token']        
        return self.token

    def logout(self, **kwargs):
        if not self.token:
            raise Exception('You have to login before to logout')            
        kwargs['json'] = {'token': self.token}
        response = self.__request(self.url + '/logout/', **kwargs)  
        self.token = None
        return response

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