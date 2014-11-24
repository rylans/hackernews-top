'''Story Schema'''

from .schema import Schema
from .field import Field

class StorySchema(Schema):
    '''Story Schema (Score, Title, By, Url)

    >>> StorySchema().get_fields()[0].get_name()
    'score'

    >>> StorySchema().get_fields()[3].get_key()
    True
    '''

    def __init__(self):
        self.fields = []
        self.fields.append(Field("score"))
        self.fields.append(Field("title"))
        self.fields.append(Field("by", volatile=False))
        self.fields.append(Field("url", key=True, volatile=False))
        self.fields.append(Field("id", volatile=False))
        self.fields.append(Field("kids"))
        self.fields.append(Field("time"))
        self.fields.append(Field("type"))

        super(StorySchema, self).assert_valid(self.fields)

    def get_fields(self):
        return self.fields

    def has_field(self, name):
        '''Return True iff this schema contains a field named 'name'

        >>> StorySchema().has_field('title')
        True

        >>> StorySchema().has_field('zzz')
        False
        '''
        return any([f.get_name() == name for f in self.fields])

    def __repr__(self):
        return "StorySchema(fields=%r)" % self.fields

if __name__ == '__main__':
    import doctest
    doctest.testmod()
