'''
Abstract class which specifies the data model of an object

Author: Rylan Santinon
'''

from abc import ABCMeta, abstractmethod

class Schema(object):
    '''Schema for data models'''
    #pylint: disable=abstract-class-not-used
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_fields(self):
        '''Get the list of fields'''
        pass

    @abstractmethod
    def has_field(self, name):
        '''Return True iff this schema contains a field named 'name' '''
        pass

    @abstractmethod
    def __repr__(self):
        '''Object representation'''
        pass

    def assert_valid(self, fields):
        '''Run all assertions'''
        self.assert_has_one_key(fields)
        self.assert_has_nonvolatile_key(fields)

    def assert_has_one_key(self, fields):
        '''Raise AssertionError if fields don't have exactly one key'''
        #pylint: disable=no-self-use
        assert len([f for f in fields if f.get_key()]) == 1

    def assert_has_nonvolatile_key(self, fields):
        '''Raise AssertionError if field has volatile key'''
        #pylint: disable=no-self-use
        assert len([f for f in fields if \
                f.get_key() and f.get_volatility()]) == 0
