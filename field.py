'''
Data field in a schema

Author: Rylan Santinon
'''

class Field(object):
    '''Schema field'''

    def __init__(self, name, key=False, volatile=True, datatype=str):
        '''Initializes field

        >>> Field('abc').get_key()
        False

        >>> Field('abc').get_volatility()
        True

        >>> Field('bar', key=True, volatile=False).get_key()
        True

        >>> Field('bar', key=True, volatile=False).get_volatility()
        False
        '''
        self.name = name
        self.key = key
        self.volatility = volatile
        self.datatype = type(datatype())

    def get_datatype(self):
        '''Returns the data type property

        >>> Field('xyz', datatype=int).get_datatype() == type(1)
        True

        >>> Field('xyz', datatype=float).get_datatype() == type(1)
        False

        >>> Field('xyz').get_datatype() == type('string')
        True
        '''
        return self.datatype

    def get_name(self):
        '''Returns the name property

        >>> f = Field('baz', True, True)
        >>> f.get_name()
        'baz'
        '''
        return self.name

    def get_key(self):
        '''Returns the key property

        >>> f = Field('baz', True, True)
        >>> f.get_key()
        True
        '''
        return self.key

    def get_volatility(self):
        '''Returns the volatility property

        >>> f = Field('baz', False, False)
        >>> f.get_volatility()
        False
        '''
        return self.volatility

    def __repr__(self):
        '''Object representation of this field

        >>> Field('foo', False, True).__repr__()
        "Field(name='foo', key=False, volatile=True)"
        '''
        return "Field(name=%r, key=%r, volatile=%r)" \
                % (self.name, self.key, self.volatility)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
