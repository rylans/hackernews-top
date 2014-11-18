'''Story Schema'''

from schema import Schema
from field import Field

class StorySchema(Schema):
    '''Story Schema (Score, Title, By, Url)

    >>> StorySchema().get_fields()[0].get_name()
    'Score'

    >>> StorySchema().get_fields()[3].get_key()
    True
    '''

    def __init__(self):
        self.fields = []
        self.fields.append(Field("Score", volatile=True))
        self.fields.append(Field("Title", volatile=True))
        self.fields.append(Field("By"))
        self.fields.append(Field("Url", key=True))

    def get_fields(self):
        return self.fields

if __name__ == '__main__':
    import doctest
    doctest.testmod()
