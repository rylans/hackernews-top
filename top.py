import urllib2
import json

def make_item_endpoint(item_id):
  return "https://hacker-news.firebaseio.com/v0/item/" + str(item_id) + ".json"

def get_top():
  endpoint_top100 = "https://hacker-news.firebaseio.com/v0/topstories.json"
  resp = urllib2.urlopen(endpoint_top100)
  rawdata = resp.read()
  article_list = json.loads(rawdata)
  return article_list

def get_item(item_id):
  url = make_item_endpoint(item_id)
  resp = urllib2.urlopen(url)
  rawdata = resp.read()
  story = json.loads(rawdata)

  score = story["score"]
  title = story["title"]
  by = story["by"]

  print "[" + str(score) + "] " + title + " (" + by + " )"
  

def main():
  article_list = get_top()

  for i in article_list[:5]:
    get_item(i)

main()
