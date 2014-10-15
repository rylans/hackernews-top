## csv_io.py
##
## Rylan Santinon

from time import strftime
import os

class CsvIo:
  def __init__(self):
    self.ext_csv = ".csv"
    self.users_dir = "users"
    self.stories_dir = "stories"

    self.users_aggregate = 'all_users.csv'
    self.stories_aggregate = 'all_stories.csv'
    self.ignore = [self.users_aggregate, self.stories_aggregate]

  def get_datetime(self):
    """Get yyyy-mm-dd formatted string

    >>> s = CsvIo().get_datetime()
    >>> len(s) == 10
    True
    """
    return strftime("%Y-%m-%d")

  def get_path(self, filename):
    """Get the proper relative path for a yyyy-mm-dd filename

    >>> CsvIo().get_path('2014-10-14.csv')
    '2014/10/2014-10-14.csv'
    """
    parts = filename.split('-')
    return os.path.join(parts[0],parts[1],filename)

  def write_stories_csv(self, stories):
    filepath = self.get_datetime() + self.ext_csv
    fullpath = os.path.join(self.stories_dir, self.get_path(filepath))
    f = open(fullpath, "w")
    f.write("SCORE,TITLE,BY,URL\n")
    for story in stories:
      story_string = self.story_to_csv(story).encode('utf-8')
      f.write(story_string)
      f.write('\n')
    f.close()

  def write_users_csv(self, users):
    filepath = self.get_datetime() + self.ext_csv
    fullpath = os.path.join(self.users_dir,self.get_path(filepath))
    f = open(fullpath, "w")
    f.write("ID,KARMA,CREATED,SUBMISSIONS\n")
    for user in users:
      user_string = self.user_to_csv(user).encode('utf-8')
      f.write(user_string)
      f.write('\n')
    f.close()

  def story_to_csv(self, story):
    #SCORE,TITLE,BY,URL
    cols = []
    cols.append(str(story["score"]))
    cols.append(story["title"])
    cols.append(story["by"])
    cols.append(story["url"])
    csv_cols = [self.remove_csv_chars(col) for col in cols]
    return ','.join(csv_cols)

  def user_to_csv(self, user):
    #ID,KARMA,CREATED,SUBMISSIONS
    cols = []
    cols.append(user["id"])
    cols.append(str(user["karma"]))
    cols.append(str(user["created"]))
    submitted = [str(s) for s in user["submitted"]]
    cols.append(str(len(submitted)))
    csv_cols = [self.remove_csv_chars(col) for col in cols]
    return ','.join(csv_cols)

  def remove_csv_chars(self, text):
    """Remove commas and quotes

    >>> CsvIo().remove_csv_chars('abc,"31,ab",z"')
    'abc31abz'
    """
    return self.remove_commas(self.remove_quotes(text))

  def remove_quotes(self, text):
    return text.replace('"','')

  def remove_commas(self, text):
    return text.replace(',','')

  def recursive_walk(self, directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
      for f in files:
	if self.ext_csv not in f:
	  continue
	if f not in self.ignore:
	  file_list.append(os.path.join(root,f))
    return file_list

  def concat_csv(self, dir, out, header):
    csvs = self.recursive_walk(dir)
    csv_lines = {}

    for csv in csvs:
      f = open(csv)
      i = 0
      for line in f.readlines():
	if i == 0:
	  i += 1
	  continue
	stripped_line = line.strip()
	csv_lines[stripped_line.split(',')[0]] = stripped_line
	#TODO: Resolve duplicates by greatest submissions
      f.close()

    line_list = [csv_lines[k] for k in csv_lines.keys()]
    sorted_lines = sorted(line_list)

    f = open(os.path.join(dir, out), "w")
    f.write(header)
    wrote = 0
    for u in sorted_lines:
      wrote += 1
      f.write(u)
      f.write('\n')
    f.close()
    return wrote

  def concat_users(self):
    """Concatenate all csv files in /users folder

    >>> w = CsvIo().concat_users()
    >>> w > 0
    True
    """
    return self.concat_csv(self.users_dir, self.users_aggregate, "ID,KARMA,CREATED,SUBMISSIONS\n")

  def concat_stories(self):
    """Concatenate all csv files in /stories folder

    >>> w = CsvIo().concat_stories()
    >>> w > 0
    True
    """
    return self.concat_csv(self.stories_dir, self.stories_aggregate, "SCORE,TITLE,BY,URL\n")

if __name__ == '__main__':
  import doctest
  doctest.testmod()
