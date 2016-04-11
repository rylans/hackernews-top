hntop Documentation
==================

# HnApi

Function | Api Endpoint | Returns
---------|--------------|--------
get_item(id) | https://hacker-news.firebaseio.com/v0/item/{id}.json | HnItem
get_user(id) | https://hacker-news.firebaseio.com/v0/user/{id}.json | HnItem
get_max_item() | https://hacker-news.firebaseio.com/v0/maxitem.json | id
get_updates() | https://hacker-news.firebaseio.com/v0/updates.json | List of ids
get_top() | https://hacker-news.firebaseio.com/v0/topstories.json | List of ids
get_new() | https://hacker-news.firebaseio.com/v0/newstories.json | List of ids
get_ask() | https://hacker-news.firebaseio.com/v0/askstories.json | List of ids
get_show() | https://hacker-news.firebaseio.com/v0/showstories.json | List of ids
get_job() | https://hacker-news.firebaseio.com/v0/jobstories.json | List of ids
get(userid_or_itemid) | either /item/ or /user/ | HnItem

# HnItem

Function | Returns
---------|--------
get(field_id, default='') | String value of field or default
is_deleted() | True if item is deleted or dead. False otherwise

This is a list of attributes an item may have. Each item has a subset of these attributes:

Attribute | Returns
---------|--------
json | dict of underlying JSON object
type | String. (comment, story, poll, etc)
by | String userid
id | Integer id
kids | List of ids
parent | id
text | String
time | Integer seconds past epoch
title | String
url | String
parts | List of ids
about | String
karma | Integer
submitted | List of ids
items | List of ids
profiles | List of userids
