"""setup.py"""
#pylint: disable=bad-continuation

from setuptools import setup, find_packages

setup(name='HN API',
    version='0.0.4',
    description='Python wrapper over HackerNews Firebase API',
    author='Rylan Santinon',
    url='https://github.com/rylans/hackernews-top',
    packages=find_packages())
