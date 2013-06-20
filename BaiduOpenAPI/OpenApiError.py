#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '1.0.0'
__author__ = 'guan hua (guanhua2011@gmail.com)'

'''
api error exception class
'''

class OpenApiError(StandardError):
    '''
    raise OpenAPI Error
    '''
    def __init__(self, error_code, error_msg):
        self.error_code = error_code
        self.error_msg = error_msg
        StandardError.__init__(self, error_code)

    def __str__(self):
        return 'OpenApiError: %s: %s' % (self.error_code, self.error_msg)
        
    def get_error_code(self):
        '''
        Get error code.
        '''
        return self.__error_code if self.__error_code else ''
        
    def get_error_msg(self):
        '''
        Get error message.
        '''
        return self.__error_msg if self.__error_msg else ''
