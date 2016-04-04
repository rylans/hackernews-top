"""Hacker News Item

Author: Rylan Santinon
"""

class HnItem(object):
    """Hacker news item

    comment:
    {
        "by": "norvig",
        "id": 2921983,
        "kids": [2922097, 2922429, 2924562],
        "parent": 2921506,
        "text": "Aw shucks.",
        "time": 1314211127
        "type": "comment"
    }

    story:
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

    poll:
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

    user:
    {
        "about" : "This is a test",
        "created" : 1173923446,
        "delay" : 0,
        "id" : "jl",
        "karma" : 2937,
        "submitted" : [8265435, 8168423, 8090326]
    }

    updates:
    {
        "items": [8423305, 8420805, 8423178],
        "profiles": ["thefox", "mdda", "neom"]
    }
    """
    def __init__(self, json):
        # dict from serialized JSON data
        self.json = json

        # add missing type for user items. used in __repr__
        if self.json.get('karma'):
            self.json['type'] = 'user'

        # add missing type for update items. used in __repr__
        if self.json.get('profiles'):
            self.json['type'] = 'update'
            self.json['id'] = self.json['items'][0]

    def is_deleted(self):
        """Return True if this item is deleted"""
        return bool(self.json.get('deleted') or self.json.get('dead'))

    def get_field_by_name(self, name):
        """Get field by name

        Parameter
        ----------
        name : str
            The name of the field

        Returns
        -------
        str
            The value held in the field

        Raises
        ------
        RuntimeError
            if `name` is not in the schema
        """
        try:
            return self.json[name]
        except KeyError:
            return ''

    def get(self, name):
        """Same as get_field_by_name"""
        return self.get_field_by_name(name)

    def __getattr__(self, key):
        try:
            return self.json[key]
        except KeyError as keyerror:
            raise AttributeError(keyerror)

    def is_special_field(self, name):
        """Return True if name is a field like 'deleted' or 'dead'"""
        return name == 'deleted' or name == 'dead'

    def __repr__(self):
        return '<HackerNews %s: %s>' % (
            self.get('type'), self.get('id'))

if __name__ == '__main__':
    import json
    userjson = """{
        "about" : "This is a test",
        "created" : 1173923446,
        "delay" : 0,
        "id" : "jl",
        "karma" : 2937,
        "submitted" : [8265435, 8168423, 8090326]
    }"""
    jsondata = json.loads(userjson)
    item = HnItem(jsondata)
    print(item)

    story = """{
        "by": "dhouston",
        "id": 8863,
        "kids": [8952, 9224, 8917],
        "score": 111,
        "time": 1175714200,
        "title": "My YC app: Dropbox - Throw away your USB drive",
        "type": "story",
        "url": "http://www.getdropbox.com/u/2/screencast.html"
    }"""
    jsonstory = json.loads(story)
    storyitem = HnItem(jsonstory)
    print(storyitem)

    updates = """{
        "items": [8423305, 8420805, 8423178],
        "profiles": ["thefox", "mdda", "neom"]
    }"""
    jsonupdates = json.loads(updates)
    updateitem = HnItem(jsonupdates)
    print(updateitem)
