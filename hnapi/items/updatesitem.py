"""
Updates Item

Example:
{
    "items": [8423305, 8420805, 8423178],
    "profiles": ["thefox", "mdda", "neom"]
}
"""

from ..schemas.updatesschema import UpdatesSchema
from .hnitem import HnItem

class UpdatesItem(HnItem):
    """Updates Item based on the abstract HnItem

    Examples
    --------

    >>> UpdatesItem({'items':[842, 239, 444]}).get_field_by_name('items')
    [842, 239, 444]
    """
    def __init__(self, json):
        self.json = json

    def get_schema(self):
        return UpdatesSchema()

    def __repr__(self):
        return "UpdatesItem(json=%r, schema=%r)" \
                % (self.json, self.get_schema())

if __name__ == '__main__':
    import doctest
    doctest.testmod(raise_on_error=True)
