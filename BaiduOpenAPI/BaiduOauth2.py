#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '1.0.0'
__author__ = 'guan hua (guanhua2011@gmail.com)'

'''
oauth client class
'''
from BaiduUtils import HttpObject
from OpenApiError import  OpenApiError

class OauthClient(object):
    def __init__(self,  client_id,  client_secret,  redirect_uri = 'oob'):
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__redirect_uri = redirect_uri
        self.__domain = 'https://openapi.baidu.com/oauth/2.0/'
        self.__http_object = HttpObject() 
        
    def get_authorize_url(self,  state = '',    scope = '',  display = 'page'): 
        '''
        Get baidu oayuth2's authorization granting url.
        ''' 
        return '%s%s?%s' % (self.__domain,  'authorize',  
                            self.__http_object.params_encode( response_type = 'code', 
                                client_id = self.__client_id,  redirect_uri = self.__redirect_uri,  
                                scope = scope, display = display, state = state))
                    
    def get_access_token_by_authorization_code(self,  code):
        '''
        Get access token ifno by authorization code.
        '''
        try:
            return self.__http_object.get('%s%s' % (self.__domain, 'token'), 
                client_id = self.__client_id, 
                client_secret = self.__client_secret, 
                redirect_uri = self.__redirect_uri, 
                code = code, 
                grant_type = 'authorization_code')
        except OpenApiError as e:
            return e
            
    def get_access_token_by_client_credentials(self,  scope = ''):
        '''
        Get access token info by client credentials.
        '''
        return self.__http_object.get('%s%s' % (self.__domain,  'token'),   
                                client_id = self.__client_id, 
                                client_secret  = self.__client_secret, 
                                scope = scope, 
                                grant_type = 'client_credentials')
                                
    def get_access_token_by_refresh_token(self,  refresh_token,  scope = ''):
        '''
        Get access token info by authorization code.
        '''
        return self.__http_object.get('%s%s' % (self.__domain,  'token'), 
                                client_id = self.__client_id, 
                                client_secret  = self.__client_secret, 
                                refresh_token = refresh_token, 
                                scope = scope, 
                                grant_type = 'refresh_token')
    
