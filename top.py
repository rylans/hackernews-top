import urllib2

endpoint_top100 = "https://hacker-news.firebaseio.com/v0/topstories.json"

resp = urllib2.urlopen(endpoint_top100)
print resp.read()
