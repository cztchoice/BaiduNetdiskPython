#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '1.0.0'
__author__ = 'Chen Zhitao (cztchoice@gmail.com)'

'''
Netdisk client class
'''
from BaiduUtils import HttpObject
from OpenApiError import  OpenApiError

class BaiduNetdisk(object):
    def __init__(self,  access_token):
        '''
        Initialize by access token.
        '''
        self.__access_token = str(access_token)
        self.__domain = 'https://pcs.baidu.com/rest/2.0/pcs/'
        self.__http_object = HttpObject() 
    def quota(self):
        '''
        Get user quota info.
        '''
        try:
            return self.__http_object.get('%s%s' % (self.__domain, 'quota'), 
                method = 'info',
                access_token = self.__access_token
                )
        except OpenApiError,  e:
            return e
    def upload_single_file(self, path_arg, file_arg, ondup_arg = "newcopy"):
        '''
        upload a single file.
        '''
        try:
            file_handler = open(file_arg, "rb")
            #print file_handler.read()
            #file_handler.seek(0)
            return self.__http_object.post_upload('%s%s' % (self.__domain, 'file'), 
                method = 'upload',
                access_token = self.__access_token,
                path = path_arg,
                file = file_handler,
                ondup = ondup_arg
                )
        except OpenApiError,  e:
            return e
