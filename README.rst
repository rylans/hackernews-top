Hacker News Top
===============

|Build Status| |Coverage Status| |Version| |License|

Unofficial Python wrapper over Hacker News' official Firebase API.

Install
-------

::

    > pip install hntop

Usage Examples
--------------

Get Item
~~~~~~~~

.. code:: python

    >>> from hnapi import ApiConnector
    >>> con = ApiConnector()
    >>> item = con.get_item(8863)
    >>> item.get('title')
    u'My YC app: Dropbox - Throw away your USB drive'
    >>> item.get('by')
    u'dhouston'

Get User
~~~~~~~~

.. code:: python

    >>> from hnapi import ApiConnector
    >>> user = ApiConnector().get_user('pg')
    >>> user.get('about')
    u'Bug Fixer.'
    >>> user.get('karma')
    155046

Top Stories
~~~~~~~~~~~

.. code:: python

    >>> from hnapi import ApiConnector
    >>> top = ApiConnector().get_top()
    >>> top
    [8959672, 8960995, 8961086, 8960029, 8960773, 8959207, 8960504, 8960280, 8960486, 8959875, 8955426, 8958731, 8961438, 8961093, 8959138]

Max Item
~~~~~~~~

.. code:: python

    >>> from hnapi import ApiConnector
    >>> con = ApiConnector()
    >>> max_item_id = con.get_max_item()
    >>> max_item_id
    8967822
    >>> max_item = con.get_item(max_item_id)
    >>> max_item.get('type')
    u'comment'
    >>> max_item.get('text')
    u'Interesting. Being partially colour blind I would have thought that the original was much greener, while the re-release is a lot bluer and..'

License
-------

Apache

.. |Build Status| image:: https://travis-ci.org/rylans/hackernews-top.svg?branch=master
   :target: https://travis-ci.org/rylans/hackernews-top
.. |Coverage Status| image:: https://coveralls.io/repos/rylans/hackernews-top/badge.svg?branch=master
   :target: https://coveralls.io/r/rylans/hackernews-top?branch=master
.. |Version| image:: https://badge.fury.io/py/hntop.svg
   :target: https://badge.fury.io/py/hntop
.. |License| image:: https://img.shields.io/pypi/l/hntop.svg
   :target: https://github.com/rylans/hackernews-top
