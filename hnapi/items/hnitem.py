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
    def is_deleted(self):
        """Return True iff this item is deleted"""
        pass

    @abstractmethod
    def get_field_by_name(self, name):
        """Return field where name == field.get_name()"""
        pass

    @abstractmethod
    def get(self, name):
        """return get_field_by_name(name)"""
        pass

    @abstractmethod
    def __repr__(self):
        pass
