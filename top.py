## top.py
## Get top stories from Hacker News' official API
##
## Rylan Santinon

import urllib2
import json

output_file = "top.out"

def write_stories(stories):
  f = open(output_file, "w")
  for story in stories:
    story_string = story_to_string(story).encode('utf-8')
    f.write(story_string)
    f.write('\n')
  f.close()

def make_item_endpoint(item_id):
  return "https://hacker-news.firebaseio.com/v0/item/" + str(item_id) + ".json"

def story_to_string(story):
  score = story["score"]
  title = story["title"]
  by = story["by"]
  return "[" + str(score) + "] " + title + " (" + by + ")"

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

  return story

def main():
  article_list = get_top()
  stories = []

  for i in article_list[:10]:
    story = get_item(i)
    print story_to_string(story)
    stories.append(story)

  write_stories(stories)


main()
