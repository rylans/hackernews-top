## api_connector.py
##
## Rylan Santinon

import urllib2
import json

class NetworkError(RuntimeError):
  def __init__(self, e):
    super(RuntimeError,self).__init__(e)

class ApiConnector:
  def __init__(self):
    pass

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
      resp = urllib2.urlopen(url)
      raw = resp.read()
      jsondata = json.loads(raw)
      return jsondata
    except urllib2.URLError as e:
      raise NetworkError(e)
    except ValueError as e:
      raise NetworkError(e)

  def get_top(self):
    """Request the top 100 stories
    
    >>> top = ApiConnector().get_top()
    >>> len(top) == 100
    True
    """
    endpoint_top100 = "https://hacker-news.firebaseio.com/v0/topstories.json"
    return self.request(endpoint_top100)

if __name__ == '__main__':
  import doctest
  doctest.testmod()
