"""
User Item

Example:
{
    "about" : "This is a test",
    "created" : 1173923446,
    "delay" : 0,
    "id" : "jl",
    "karma" : 2937,
    "submitted" : [8265435, 8168423, 8090326]
}
"""

from ..schemas.userschema import UserSchema
from .hnitem import HnItem

class UserItem(HnItem):
    """
    User Item based on the abstract HnItem

    Examples
    --------

    >>> UserItem({'id':1234}).get_field_by_name('id')
    1234

    >>> UserItem({'id':'abc'}).get('id')
    'abc'

    >>> UserItem({'id':1234}).get_field_by_name('foobar') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    RuntimeError: No field named 'foobar' in ...

    >>> UserItem({'deleted':'True'}).is_deleted()
    True

    >>> UserItem({'dead':'True'}).is_deleted()
    True

    >>> UserItem({}).is_deleted()
    False
    """

    def __init__(self, json):
        self.json = json

    def get_schema(self):
        return UserSchema()

    def __repr__(self):
        return "UserItem(json=%r, schema=%r)" \
                % (self.json, self.get_schema())

if __name__ == '__main__':
    import doctest
    doctest.testmod()
