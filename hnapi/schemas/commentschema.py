"""
Comment Schema

"""
from .schema import Schema
from .field import Field

class CommentSchema(Schema):
    """Comment schema"""

    def __init__(self):
        self.fields = []
        self.fields.append(Field("id", volatile=False, key=True))
        self.fields.append(Field("by", volatile=False))
        self.fields.append(Field("parent", volatile=False))
        self.fields.append(Field("kids"))
        self.fields.append(Field("time", volatile=False))
        self.fields.append(Field("type"))
        self.fields.append(Field("text"))

        super(CommentSchema, self).assert_valid(self.fields)

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

        >>> CommentSchema().has_field('text')
        True

        >>> CommentSchema().has_field('zzz')
        False
        """
        return any([f.get_name() == name for f in self.fields])

    def __repr__(self):
        return "CommentSchema(fields=%r)" % self.fields

if __name__ == '__main__':
    import doctest
    doctest.testmod(raise_on_error=True)
