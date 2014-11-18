'''
Abstract class which specifies the data model of an object

Author: Rylan Santinon
'''

from abc import ABCMeta, abstractmethod

class Schema(object):
    '''Schema for data models'''
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_fields(self):
        '''Get the list of fields'''
        pass
