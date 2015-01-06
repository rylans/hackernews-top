"""Comment item

Example:
{
    "by": "norvig",
    "id": 2921983,
    "kids": [2922097, 2922429, 2924562],
    "parent": 2921506,
    "text": "Aw shucks.",
    "time": 1314211127
    "type": "comment"
}

Author: Rylan Santinon
"""

from ..schemas.commentschema import CommentSchema
from .hnitem import HnItem

class CommentItem(HnItem):
    """Comment Item based on the abstract HnItem

    Examples
    --------

    >>> CommentItem({'id':1234}).get_field_by_name('id')
    1234

    >>> CommentItem({'id':'abc'}).get('id')
    'abc'

    >>> CommentItem({'id':1234}).get_field_by_name('foobar') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    RuntimeError: No field named 'foobar' in ...

    >>> CommentItem({'deleted':'True'}).is_deleted()
    True

    >>> CommentItem({'dead':'True'}).is_deleted()
    True

    >>> CommentItem({}).is_deleted()
    False
    """

    def __init__(self, json):
        self.json = json

    def get_schema(self):
        return CommentSchema()

    def __repr__(self):
        return "CommentItem(json=%r, schema=%r)" \
                % (self.json, self.get_schema())

if __name__ == '__main__':
    import doctest
    doctest.testmod(raise_on_error=True)
