"""Story Item"""

from storyschema import StorySchema
from hnitem import HnItem

class StoryItem(HnItem):
    """Story Item"""

    def __init__(self, json):
        self.json = json

    def get_schema(self):
        return StorySchema()

    #pylint: disable=line-too-long
    def get_field_by_name(self, name):
        """Get field by name

        >>> StoryItem({'id':1234}).get_field_by_name('id')
        1234

        >>> StoryItem({'id':1234}).get_field_by_name('foobar') # doctest: +ELLIPSIS
        Traceback (most recent call last):
        RuntimeError: No field named 'foobar' in ...
        """
        schema = self.get_schema()
        if schema.has_field(name):
            return self.json[name]
        else:
            raise RuntimeError("No field named %r in %r" \
                    % (name, schema))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
