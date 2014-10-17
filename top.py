"""
Hacker News Top:
  -Get top stories from Hacker News' official API
  -Record all users who comment on those stories

Author: Rylan Santinon
"""

from api_connector import *
from csv_io import *

def main():
  conn = ApiConnector()
  csvio = CsvIo()
  article_list = conn.get_top()
  stories = []

  for i in article_list:
    try:
      story = conn.get_item(i)
      if story.get("deleted"):
	continue
      print csvio.story_to_csv(story)
      stories.append(story)
    except NetworkError as e:
      print e

  csvio.write_stories_csv(stories)

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

  csvio.write_users_csv(users)

if __name__ == '__main__':
  csvio = CsvIo()
  main()
  csvio.concat_users()
  csvio.concat_stories()
