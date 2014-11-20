"""Abstract Hacker News Item

Author: Rylan Santinon
"""

from abc import ABCMeta, abstractmethod

#pylint: disable=abstract-class-not-used
class HnItem(object):
    """Abstract item"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_schema(self):
        """Return the item's schema"""
        pass

    @abstractmethod
    def get_field_by_name(self, name):
        """Return field where name == field.get_name()"""
        pass
