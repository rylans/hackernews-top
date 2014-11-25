"""
Wrapper for the Hacker News API
Supports requests for:
  -Story items
  -Users

Author: Rylan Santinon
"""

try:
    #pylint: disable= no-name-in-module, import-error
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json
import logging
from ..items.storyitem import StoryItem

class NetworkError(RuntimeError):
    """Runtime errors for http calls and json parsing

    >>> raise NetworkError('foo')
    Traceback (most recent call last):
    NetworkError: foo
    """
    def __init__(self, e):
        super(NetworkError, self).__init__(e)

class ApiConnector(object):
    '''Connects to HackerNews API and provides the schema'''
    def __init__(self):
        self.user_dict = {}
        self.logger = logging.getLogger(__name__)
        self.timeout = 35

    def set_timeout(self, time):
        """Set the timeout in seconds for the urllib2.urlopen call

        >>> ApiConnector().set_timeout(3.551).timeout == 3.551
        True

        >>> ApiConnector().set_timeout(-2)
        Traceback (most recent call last):
        RuntimeError: Timeout must be non-negative
        """
        if time < 0:
            raise RuntimeError("Timeout must be non-negative")
        self.timeout = time
        return self

    #pylint: disable=line-too-long, invalid-name
    def request(self, url):
        """Request json data from the URL

        >>> j = ApiConnector().request('https://hacker-news.firebaseio.com/v0/item/1.json')
        >>> j['by'] == 'pg'
        True

        >>> ApiConnector().request('https://hacker-news.firebaseio.com/v0/foobar/1.json')
        Traceback (most recent call last):
        NetworkError: HTTP Error 401: Unauthorized

        >>> ApiConnector().request('http://www.yahoo.co.jp') # doctest: +ELLIPSIS
        Traceback (most recent call last):
        NetworkError: ...
        """
        try:
            resp = urllib2.urlopen(url, timeout=self.timeout)
            jsondata = json.loads(resp.read().decode('utf-8'))
            return jsondata
        except urllib2.URLError as e:
            self.logger.exception(e)
            raise NetworkError(e)
        except ValueError as e:
            self.logger.exception(e)
            raise NetworkError(e)
        except Exception as e:
            self.logger.exception(e)
            raise NetworkError(e)
        finally:
            self.logger.debug("Requested %s", url)

    def get_top(self):
        """Request the top 100 stories
        >>> top = ApiConnector().get_top()
        >>> len(top) == 100
        True
        """
        endpoint_top100 = "https://hacker-news.firebaseio.com/v0/topstories.json"
        try:
            return self.request(endpoint_top100)
        except NetworkError:
            return []

    #pylint: disable=no-self-use, unused-variable
    def make_item_endpoint(self, item_id):
        """Return the API URL for the given item_id

        >>> ApiConnector().make_item_endpoint(1)
        'https://hacker-news.firebaseio.com/v0/item/1.json'

        >>> ApiConnector().make_item_endpoint(None)
        Traceback (most recent call last):
        RuntimeError: Parameter None must be an integer

        >>> ApiConnector().make_item_endpoint('baz')
        Traceback (most recent call last):
        RuntimeError: Parameter baz must be an integer
        """
        try:
            int(item_id)
        except (TypeError, ValueError) as e:
            raise RuntimeError("Parameter %s must be an integer" % item_id)
        return "https://hacker-news.firebaseio.com/v0/item/" + str(item_id) + ".json"

    def make_user_endpoint(self, username):
        """Return the API URL for the given username

        >>> ApiConnector().make_user_endpoint('pg')
        'https://hacker-news.firebaseio.com/v0/user/pg.json'
        """
        return "https://hacker-news.firebaseio.com/v0/user/" + username + ".json"

    def build_hnitem(self, item_json):
        """Build an instance of hnitem depending on the type"""
        if item_json['type'] == "story" or item_json['type'] == 'job':
            return StoryItem(item_json)
        raise RuntimeError("Item type unsupported: %r" % item_json)

    def get_item(self, item_id):
        """Get a particular item by item's id

        >>> it = ApiConnector().get_item(1)
        >>> it.get_field_by_name('by') == 'pg'
        True
        """
        url = self.make_item_endpoint(item_id)
        story = self.request(url)
        if story != None and story.get("by"):
            by = str(story["by"])
            self.user_dict[by] = by
        return self.build_hnitem(story)

    def get_user(self, username):
        """Get a user by username

        >>> u = ApiConnector().get_user('pg')
        >>> u['id'] == 'pg'
        True
        """
        url = self.make_user_endpoint(username)
        return self.request(url)

    #pylint: disable=logging-not-lazy
    def get_kids_recur(self, kids, level):
        """Recursive helper method for retrieving kids in comments"""
        for k in [str(k) for k in kids]:
            url = self.make_item_endpoint(k)
            jdata = self.request(url)
            if jdata == None or not jdata.get("by"):
                continue
            by = str(jdata["by"])
            self.user_dict[by] = by
            self.logger.debug("Found user: %s at level: %s" % (by, level))
            if jdata.get("kids"):
                self.get_kids_recur(jdata["kids"], level + 1)

    def get_kids(self, story):
        """Get all usernames from comments of a story

        >>> o = ApiConnector().get_kids({'kids':[1]})
        >>> len(o.keys()) == 10
        True
        """
        story = story.json
        if story == None or not story.get("kids"):
            return
        kids = story["kids"]
        self.get_kids_recur(kids, 0)
        return self.user_dict

    def is_api_item(self, obj):
        '''Returns true iff obj is an HN item

        >>> ApiConnector().is_api_item({'id':321})
        True

        >>> ApiConnector().is_api_item(None)
        False

        >>> ApiConnector().is_api_item({'id':123, 'deleted':'True'})
        True
        '''
        if obj == None:
            return False
        return not not obj.get('id') or obj.get_field_by_name('id')

    def is_valid_item(self, obj):
        '''Returns true iff obj is an undeleted HN item

        >>> ApiConnector().is_valid_item({'id':123})
        True

        >>> ApiConnector().is_valid_item(None)
        False

        >>> ApiConnector().is_valid_item({'id':123, 'deleted':'True'})
        False
        '''
        return self.is_api_item(obj) and not obj.is_deleted()

if __name__ == '__main__':
    import doctest
    logging.disable(logging.CRITICAL)
    doctest.testmod()
    logging.disable(logging.NOTSET)
