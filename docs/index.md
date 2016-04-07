hntop Documentation
==================

# HnApi

Function | Api Endpoint | Returns
---------|--------------|--------
get_item(id) | https://hacker-news.firebaseio.com/v0/item/{id}.json | HnItem
get_user(id) | https://hacker-news.firebaseio.com/v0/user/{id}.json | HnItem
get_updates() | https://hacker-news.firebaseio.com/v0/updates.json | List of ids
get_max_item() | https://hacker-news.firebaseio.com/v0/maxitem.json | id
get_top() | https://hacker-news.firebaseio.com/v0/topstories.json | List of ids
get_new() | https://hacker-news.firebaseio.com/v0/newstories.json | List of ids
get() | either /item/ or /user/ | HnItem


# HnItem

Document HnItem
