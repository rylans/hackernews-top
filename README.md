Hacker News Top
==============

[![Build Status](https://travis-ci.org/rylans/hackernews-top.svg?branch=master)](https://travis-ci.org/rylans/hackernews-top) [![Coverage Status](https://coveralls.io/repos/rylans/hackernews-top/badge.svg?branch=master)](https://coveralls.io/r/rylans/hackernews-top?branch=master)

Unofficial Python wrapper over Hacker News' official Firebase API.

## Install

```
> git clone https://github.com/rylans/hackernews-top.git
> cd hackernews-top
> pip install .
```

## Usage Examples

### Get Item

```
>>> from hnapi.connectors.api_connector import ApiConnector
>>> con = ApiConnector()
>>> item = con.get_item(8863)
>>> item.get('title')
u'My YC app: Dropbox - Throw away your USB drive'
>>> item.get('by')
u'dhouston'
```

### Get User

```
>>> from hnapi.connectors.api_connector import ApiConnector
>>> user = ApiConnector().get_user('pg')
>>> user.get('about')
u'Bug Fixer.'
>>> user.get('karma')
155046
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

## Statistical Data

![Domain Frequency](diagrams/frequency_bar.png)

## License

Apache
