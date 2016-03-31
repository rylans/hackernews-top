Hacker News Top
==============

[![Build Status](https://travis-ci.org/rylans/hackernews-top.svg?branch=master)](https://travis-ci.org/rylans/hackernews-top) [![Coverage Status](https://coveralls.io/repos/rylans/hackernews-top/badge.svg?branch=master)](https://coveralls.io/r/rylans/hackernews-top?branch=master) [![Version](https://badge.fury.io/py/hntop.svg)](https://badge.fury.io/py/hntop) [![License](https://img.shields.io/pypi/l/hntop.svg)](https://github.com/rylans/hackernews-top)

Unofficial Python wrapper over Hacker News' official Firebase API.

## Install

```
> git clone https://github.com/rylans/hackernews-top.git
> cd hackernews-top
> pip install .
```

## Usage Examples

### Get Item

```python
>>> from hnapi.connectors.api_connector import ApiConnector
>>> con = ApiConnector()
>>> item = con.get_item(8863)
>>> item.get('title')
u'My YC app: Dropbox - Throw away your USB drive'
>>> item.get('by')
u'dhouston'
```

### Get User

```python
>>> from hnapi.connectors.api_connector import ApiConnector
>>> user = ApiConnector().get_user('pg')
>>> user.get('about')
u'Bug Fixer.'
>>> user.get('karma')
155046
```

### Top Stories

```python
>>> from hnapi.connectors.api_connector import ApiConnector
>>> top = ApiConnector().get_top()
>>> top
[8959672, 8960995, 8961086, 8960029, 8960773, 8959207, 8960504, 8960280, 8960486, 8959875, 8955426, 8958731, 8961438, 8961093, 8959138, 8959621, 8958867, 8959989, 8958591, 8960902, 8961006, 8958290, 8958059, 8957385, 8960445, 8960933, 8960064, 8956245, 8960211, 8954655, 8959967, 8959377, 8961127, 8958082, 8955771, 8958248, 8955310, 8960929, 8959850, 8959720, 8958728, 8961374, 8958131, 8954737, 8961220, 8959279, 8960063, 8954353, 8956129, 8954630, 8958173, 8961079, 8954568, 8960605, 8957090, 8960824, 8959497, 8960667, 8953545, 8961237, 8955212, 8954814, 8960460, 8954544, 8955130, 8953633, 8955172, 8953512, 8961336, 8958668, 8958719, 8960062, 8960702, 8954424, 8954348, 8959596, 8960909, 8960875, 8961027, 8956313, 8960215, 8960301, 8955663, 8954687, 8958267, 8960360, 8959477, 8958233, 8955076, 8957010, 8961232, 8960303, 8960600, 8955628, 8952959, 8958604, 8954623, 8960168, 8956922, 8952100]
```

### Max Item

```python
>>> from hnapi.connectors.api_connector import ApiConnector
>>> con = ApiConnector()
>>> max_item_id = con.get_max_item()
>>> max_item_id
8967822
>>> max_item = con.get_item(max_item_id)
>>> max_item.get('type')
u'comment'
>>> max_item.get('text')
u'Interesting. Being partially colour blind I would have thought that the original was much greener, while the re-release is a lot bluer and bumped up the brightness contrast.<p>For example, most of the agent scenes in that comparison the left frame appears &quot;greener&quot; (but also more washed out in terms of brightness contrast) than the right.'
```

## Roadmap

* Item types:
  * ~~Story~~ **Done**
  * Comment **Partial support**
  * Job **Partial support**
  * Ask HN **Partial support**
  * Poll **Partial support**
* User **Partial support**
* API calls
  * ~~`v0/item`~~ **Done**
  * ~~`v0/user`~~ **Done**
  * ~~`v0/topstories`~~ **Done**
  * `v0/maxitem` **Partial support**
  * ~~`v0/updates`~~ **Done**
* Schema assertions

## License

Apache
