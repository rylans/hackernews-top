'''User Schema'''

from schema import Schema
from field import Field

class UserSchema(Schema):
    '''User schema'''

    def __init__(self):
        self.fields = []
        self.fields.append(Field("id", key=True, volatile=False))
        self.fields.append(Field("karma", datatype=int))
        self.fields.append(Field("created", volatile=False, datatype=int))
        self.fields.append(Field("submitted", datatype=list))
        self.fields.append(Field("about", datatype=str))
        self.fields.append(Field("delay", datatype=int))

        super(UserSchema, self).assert_valid(self.fields)

    def get_fields(self):
        return self.fields

    def has_field(self, name):
        '''Return True iff this schema contains a field named 'name'

        >>> UserSchema().has_field('id')
        True

        >>> UserSchema().has_field('zzz')
        False
        '''
        return any([f.get_name() == name for f in self.fields])

    def __repr__(self):
        return "UserSchema(fields=%r)" % (self.fields)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
