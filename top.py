## top.py
## Get top stories from Hacker News' official API
##
## Rylan Santinon

import urllib2
import json
from time import strftime

ext_out = ".out"
ext_csv = ".csv"

def get_datetime():
  return strftime("%Y-%m-%d")

def write_stories(stories):
  output_file = get_datetime() + ext_out
  f = open(output_file, "w")
  for story in stories:
    story_string = story_to_string(story).encode('utf-8')
    f.write(story_string)
    f.write('\n')
  f.close()

def write_stories_csv(stories):
  output_csv = get_datetime() + ext_csv
  f = open(output_csv, "w")
  f.write("SCORE,TITLE,BY,URL\n")
  for story in stories:
    story_string = story_to_csv(story).encode('utf-8')
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

def remove_csv_chars(text):
  return remove_commas(remove_quotes(text))

def remove_quotes(text):
  return text.replace('"','')

def remove_commas(text):
  return text.replace(',','')

def story_to_csv(story):
  cols = []
  cols.append(str(story["score"]))
  cols.append(story["title"])
  cols.append(story["by"])
  cols.append(story["url"])
  csv_cols = [remove_csv_chars(col) for col in cols]
  return ','.join(csv_cols)

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

  return story

def main():
  article_list = get_top()
  stories = []

  for i in article_list:
    story = get_item(i)
    print story_to_string(story)
    stories.append(story)

  write_stories(stories)
  write_stories_csv(stories)

main()
