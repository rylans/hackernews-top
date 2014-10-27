"""
Wrapper for the Hacker News API
Supports requests for:
  -Story items
  -Users

Author: Rylan Santinon
"""

import urllib2
import json
import logging

class NetworkError(RuntimeError):
  """Runtime errors for http calls and json parsing

  >>> raise NetworkError('foo')
  Traceback (most recent call last):
  NetworkError: foo
  """
  def __init__(self, e):
    super(RuntimeError,self).__init__(e)

class ApiConnector:
  def __init__(self):
    self.user_dict = {}
    self.logger = logging.getLogger(__name__)

  def request(self, url):
    """Request json data from the URL

    >>> j = ApiConnector().request('https://hacker-news.firebaseio.com/v0/item/1.json')
    >>> j['by'] == 'pg'
    True

    >>> ApiConnector().request('https://hacker-news.firebaseio.com/v0/foobar/1.json')
    Traceback (most recent call last):
    NetworkError: HTTP Error 401: Unauthorized

    >>> ApiConnector().request('http://www.yahoo.co.jp')
    Traceback (most recent call last):
    NetworkError: No JSON object could be decoded
    """
    try:
      resp = urllib2.urlopen(url, timeout = 2)
      raw = resp.read()
      jsondata = json.loads(raw)
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
    return self.request(endpoint_top100)

  def make_item_endpoint(self, item_id):
    return "https://hacker-news.firebaseio.com/v0/item/" + str(item_id) + ".json"

  def make_user_endpoint(self, username):
    return "https://hacker-news.firebaseio.com/v0/user/" + username + ".json"

  def get_item(self, item_id):
    """Get a particular item by item's id

    >>> it = ApiConnector().get_item(1)
    >>> it['by'] == 'pg'
    True
    """
    url = self.make_item_endpoint(item_id)
    story = self.request(url)
    if story.get("by"):
      by = str(story["by"])
      self.user_dict[by] = by
    return story

  def get_user(self, username):
    """Get a user by username

    >>> u = ApiConnector().get_user('pg')
    >>> u['id'] == 'pg'
    True
    """
    url = self.make_user_endpoint(username)
    return self.request(url)

  def get_kids_recur(self, kids, level):
    for k in [str(k) for k in kids]:
      url = self.make_item_endpoint(k)
      jdata = self.request(url)
      if not jdata.get("by"):
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
    if not story.get("kids"):
      return
    kids = story["kids"]
    self.get_kids_recur(kids, 0)
    return self.user_dict

if __name__ == '__main__':
  import doctest
  logging.disable(logging.CRITICAL)
  doctest.testmod()
  logging.disable(logging.NOTSET)
