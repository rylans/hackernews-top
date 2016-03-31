#!/usr/bin/env python
"""setup.py"""
# pylint: disable=bad-continuation

from setuptools import setup, find_packages

setup(name='hntop',
      version='0.0.5',
      description='Python wrapper over HackerNews Firebase API',
      author='Rylan Santinon',
      author_email='rylans@gmail.com',
      url='https://github.com/rylans/hackernews-top',
      keywords=['hn', 'hackernews', 'hnapi', 'hackernews top'],
      packages=find_packages())
