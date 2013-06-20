#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '1.0.0'
__author__ = 'guan hua (guanhua2011@gmail.com)'

from BaiduOauth2 import OauthClient
from BaiduApiClient import BaiduApiClient
from OpenApiError import OpenApiError
from BaiduUtils import BaiduUtils
from BaiduUtils import HttpObject

class Baidu():
    def __init__(self,  client_id,  client_secret,  redirect_uri = 'oob'):
        '''
        Constructor.
        '''
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__redirect_uri = redirect_uri
        self.__oauth_client = None
        self.__api_client = None
        self.__logout_domain = 'https://openapi.baidu.com/connect/2.0/logout'
        self.__http_object = HttpObject()
        self.__utils = BaiduUtils()
        
    def get_baidu_oauth2_server(self):
        '''
        Get an instance of Baidu OauthClient class.
        '''
        if not self.__oauth_client:
            self.__oauth_client = OauthClient(self.__client_id,  self.__client_secret,  self.__redirect_uri)
        return self.__oauth_client
        
    def get_baidu_api_client_server(self):
        '''
        Get an instance of BaiduApiClient class
        '''
        if not self.__api_client:
            self.__api_client = BaiduApiClient()
        return self.__api_client

    def get_logged_in_user(self,  access_token,  bd_user = None,  bd_sign = None):
        '''
        Get currently logged in user's info.
        '''
        api_client = self.get_baidu_api_client_server()
        user = api_client.api('https://openapi.baidu.com/rest/2.0/passport/users/getLoggedInUser',  
                                     access_token = access_token)
        if bd_sign and bd_user:
            params = {}
            params['bd_user'] = bd_user
            sign = self.__utils.generate_sign(params,  self.__client_secret)
            if sign != bd_sign or bd_user != user['uid']:
                return None
        return user        
    
    def get_login_url(self,  state = '',  scope ='',  display = 'page'):
        '''
        Get a Login URL for user with redirects. By default, full page redirect is	    
        assumed. If you are using the generated URL with a window.open() call in
        JavaScript, you can pass in display=popup as part of the $params.
        '''
        oauth_client = self.get_baidu_oauth2_server()
        return oauth_client.get_authorize_url(scope,  state,  display)
        
    def get_logout_url(self,  access_token,  next):
        '''
        Get a Logout URL suitable for user with redirects.
        '''
        
        return '%s?%s' % (self.__logout_domain,  
                          self.__http_object.params_encode(access_token = access_token,  next = next))
