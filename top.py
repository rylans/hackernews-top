## top.py
## -Get top stories from Hacker News' official API
## -Record all users who comment on those stories
##
## Rylan Santinon

from time import strftime
from api_connector import *
import os

ext_out = ".out"
ext_csv = ".csv"

users_dir = "users"
stories_dir = "stories"


def get_datetime():
  return strftime("%Y-%m-%d")

def get_path(filename):
  #If file is 2014-10-14.csv then return 2014/10/2014-10-14.csv
  parts = filename.split('-')
  return os.path.join(parts[0],parts[1],filename)
  
def write_stories(stories):
  filepath = get_datetime() + ext_out
  fullpath = os.path.join(stories_dir,get_path(filepath))
  f = open(fullpath, "w")
  for story in stories:
    story_string = story_to_string(story).encode('utf-8')
    f.write(story_string)
    f.write('\n')
  f.close()

def write_stories_csv(stories):
  filepath = get_datetime() + ext_csv
  fullpath = os.path.join(stories_dir,get_path(filepath))
  f = open(fullpath, "w")
  f.write("SCORE,TITLE,BY,URL\n")
  for story in stories:
    story_string = story_to_csv(story).encode('utf-8')
    f.write(story_string)
    f.write('\n')
  f.close()

def write_users_csv(users):
  filepath = get_datetime() + ext_csv
  fullpath = os.path.join(users_dir,get_path(filepath))
  f = open(fullpath, "w")
  f.write("ID,KARMA,CREATED,SUBMISSIONS\n")
  for user in users:
    user_string = user_to_csv(user).encode('utf-8')
    f.write(user_string)
    f.write('\n')
  f.close()
  
def story_to_string(story):
  try:
    score = story["score"]
    title = story["title"]
    by = story["by"]
  except KeyError as e:
    print story
    raise e

  return "[" + str(score) + "] " + title + " (" + by + ")"

def user_to_string(user):
  name = user["id"]
  karma = str(user["karma"])
  created = str(user["created"])
  submitted = [str(s) for s in user["submitted"]]
  submissions = str(len(submitted))

  return name + " (" + karma + ") <" + created + "> " + submissions

def remove_csv_chars(text):
  return remove_commas(remove_quotes(text))

def remove_quotes(text):
  return text.replace('"','')

def remove_commas(text):
  return text.replace(',','')

def story_to_csv(story):
  #SCORE,TITLE,BY,URL
  cols = []
  cols.append(str(story["score"]))
  cols.append(story["title"])
  cols.append(story["by"])
  cols.append(story["url"])
  csv_cols = [remove_csv_chars(col) for col in cols]
  return ','.join(csv_cols)

def user_to_csv(user):
  #ID,KARMA,CREATED,SUBMISSIONS
  cols = []
  cols.append(user["id"])
  cols.append(str(user["karma"]))
  cols.append(str(user["created"]))
  submitted = [str(s) for s in user["submitted"]]
  cols.append(str(len(submitted)))
  csv_cols = [remove_csv_chars(col) for col in cols]
  return ','.join(csv_cols)

def recursive_walk(directory):
  IGNORE = ['all_users.csv']
  file_list = []
  for root, dirs, files in os.walk(directory):
    for f in files:
      if f not in IGNORE:
        file_list.append(os.path.join(root,f))
  return file_list

def concat_users():
  print "concat_users"

  user_csvs = recursive_walk(users_dir)
  user_lines = {}

  for user_csv in user_csvs:
    f = open(user_csv)
    i = 0
    for line in f.readlines():
      if i == 0:
        i += 1
        continue
      stripped_line = line.strip()
      user_lines[stripped_line.split(',')[0]] = stripped_line
      #TODO: Resolve duplicates by greatest submissions
      
    f.close()

  line_list = [user_lines[k] for k in user_lines.keys()]
  sorted_users = sorted(line_list)

  f = open(os.path.join(users_dir,'all_users.csv'), "w")
  f.write("ID,KARMA,CREATED,SUBMISSIONS\n")
  for u in sorted_users:
    f.write(u)
    f.write('\n')
  f.close()

def main():
  conn = ApiConnector()
  article_list = conn.get_top()
  stories = []

  for i in article_list:
    try:
      story = conn.get_item(i)
      if story.get("deleted"):
	continue
      print story_to_string(story)
      stories.append(story)
    except NetworkError as e:
      print e

  write_stories(stories)
  write_stories_csv(stories)

  for story in stories:
    try:
      conn.get_kids(story)
    except NetworkError as e:
      print e

  users = []
  for u in sorted(conn.user_dict.keys()):
    try:
      userjson = conn.get_user(u)
      users.append(userjson)
      print u
    except NetworkError as e:
      print e

  write_users_csv(users)

if __name__ == '__main__':
  main()
  concat_users()
