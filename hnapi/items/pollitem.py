"""Poll item

Example:
{
    "by": "robg",
    "id": 7059569,
    "kids": [7059793,7059744],
    "text": "",
    "title: "Poll: As a founder, what is your salary?",
    "time": 1389732227,
    "parts": [7059570, 7059571, 7059572],
    "type": "poll",
    "score": 161
}
"""
from ..schemas.pollschema import PollSchema
from .hnitem import HnItem

class PollItem(HnItem):
    """Poll Item based on the abstract HnItem

    Examples
    --------

    >>> PollItem({'id':1234}).get_field_by_name('id')
    1234

    >>> PollItem({'id':'abc'}).get('id')
    'abc'

    >>> PollItem({'id':1234}).get_field_by_name('foobar') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    RuntimeError: No field named 'foobar' in ...

    >>> PollItem({'deleted':'True'}).is_deleted()
    True

    >>> PollItem({'dead':'True'}).is_deleted()
    True

    >>> PollItem({}).is_deleted()
    False
    """

    def __init__(self, json):
        self.json = json

    def get_schema(self):
        return PollSchema()

    def __repr__(self):
        return "PollItem(json=%r, schema=%r)" \
                % (self.json, self.get_schema())

if __name__ == '__main__':
    import doctest
    doctest.testmod(raise_on_error=True)
