#!/usr/bin/env python

from codecs import open

from setuptools import setup, find_packages

def read(f):
    return open(f, encoding='utf-8').read()

setup(name='hntop',
      version='0.0.10',
      description='Python wrapper over HackerNews Firebase API',
      long_description=read('README.rst'),
      author='Rylan Santinon',
      author_email='rylans@gmail.com',
      url='https://github.com/rylans/hackernews-top',
      keywords=['hn', 'hackernews', 'hnapi', 'hackernews top'],
      license='Apache',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Utilities',
          'Topic :: Internet :: WWW/HTTP :: Indexing/Search'],
      packages=find_packages())
