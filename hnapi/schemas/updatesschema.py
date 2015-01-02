"""
Updates Schema
"""

from .schema import Schema
from .field import Field

class UpdatesSchema(Schema):
    """Updates Schema (Items, Profiles)

    Examples
    --------

    >>> UpdatesSchema().get_fields()[0].get_name()
    'items'
    """
    def __init__(self):
        self.fields = []
        self.fields.append(Field("items"))
        self.fields.append(Field("profiles"))

    def get_fields(self):
        return self.fields

    def has_field(self, name):
        """Return True iff this schema contains a field named 'name'

        Parameters
        ----------
        name : str
            Name of the field if it exists

        Returns
        -------
        bool
            True if this schema contains `name`, False otherwise

        Examples
        --------

        >>> UpdatesSchema().has_field('items')
        True

        >>> UpdatesSchema().has_field('zzz')
        False
        """
        return any([f.get_name() == name for f in self.fields])

    def __repr__(self):
        return "UpdatesSchema(fields=%r)" % self.fields

if __name__ == '__main__':
    import doctest
    doctest.testmod(raise_on_error=True)
