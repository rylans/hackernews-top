"""Story Item

Example:
{
    "by": "dhouston",
    "id": 8863,
    "kids": [8952, 9224, 8917],
    "score": 111,
    "time": 1175714200,
    "title": "My YC app: Dropbox - Throw away your USB drive",
    "type": "story",
    "url": "http://www.getdropbox.com/u/2/screencast.html"
}

Author: Rylan Santinon
"""

from ..schemas.storyschema import StorySchema
from .hnitem import HnItem


class StoryItem(HnItem):
    """Story Item based on the abstract HnItem

    Examples
    --------

    >>> StoryItem({'id':1234}).get_field_by_name('id')
    1234

    >>> StoryItem({'id':'abc'}).get('id')
    'abc'

    >>> StoryItem({'id':1234}).get_field_by_name('foobar') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    RuntimeError: No field named 'foobar' in ...

    >>> StoryItem({'deleted':'True'}).is_deleted()
    True

    >>> StoryItem({'dead':'True'}).is_deleted()
    True

    >>> StoryItem({}).is_deleted()
    False
    """

    def __init__(self, json):
        self.json = json

    def get_schema(self):
        return StorySchema()

    def __repr__(self):
        return '<story#%s: %s>' % (str(self.get('id')), self.get('title'))

if __name__ == '__main__':
    import doctest
    doctest.testmod(raise_on_error=True)
