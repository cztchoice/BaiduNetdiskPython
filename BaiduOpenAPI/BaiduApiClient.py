#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '1.0.0'
__author__ = 'guan hua (guanhua2011@gmail.com)'

'''
api client class
'''
from BaiduUtils import HttpObject
from OpenApiError import  OpenApiError

class BaiduApiClient(object):
    def __init__(self):
        self.__http_object = HttpObject()
    
    def __call(self,  url,  http_type,  **params):
        method = http_type.lower()
        try:
            if method == 'get':
                return self.__http_object.get(url,  **params)
            else:
                return self.__http_object.post(url,  ** params)
        except OpenApiError,  e:
            return e    
    
    def api(self,  url,  http_type = 'get',  **params):
        '''
        Call an api which is opened by Baidu, file upload apis should not 
        be called by this interface
        '''
        return self.__call(url, http_type,  **params)
        
    def upload(self,  url,  **params):
        '''
        Call a file upload api.
        '''
        try:
            return self.__http_object.upload(url,  **params)
        except OpenApiError,  e:
            return e 
