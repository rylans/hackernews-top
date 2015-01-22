"""
Tests
"""
from __future__ import unicode_literals

import unittest

from hnapi.connectors.api_connector import ApiConnector

#pylint: disable=too-many-public-methods
class HnapiTest(unittest.TestCase):
    """
    Test hnapi
    """
    def test_get_item_by(self):
        """
        Test item retrieval and 'by' field
        """
        con = ApiConnector()
        item = con.get_item(8863)
        byline = item.get('by')
        self.assertEqual(byline, 'dhouston')

    def test_get_max_item(self):
        """
        Test retrieval of the max item without error
        """
        con = ApiConnector()
        max_item_id = con.get_max_item()
        max_item = con.get_item(max_item_id)
        self.assertTrue(max_item.get('id') > 0)

    def test_get_updates_users(self):
        """
        Test retrieval of new users
        """
        con = ApiConnector()
        updates = con.get_updates()
        self.assertTrue(len(updates.get('profiles')) > 1)
        user = con.get_user(updates.get('profiles')[0])
        year_2001 = 1000000000
        self.assertTrue(user.get('created') > year_2001)

    def test_get_updates_item(self):
        """
        Test retrieval of new items
        """
        con = ApiConnector()
        updates = con.get_updates()
        self.assertTrue(len(updates.get('items')) > 1)
        item = con.get_item(updates.get('items')[0])
        year_2001 = 1000000000
        self.assertTrue(item.get('time') > year_2001)

    def test_get_top(self):
        """
        Test retrieval of first and last items from /top endpoint
        """
        con = ApiConnector()
        top = con.get_top()
        self.assertTrue(len(top) == 100)

        item_0 = con.get_item(top[0])
        self.assertTrue(con.is_valid_item(item_0))

        item_100 = con.get_item(top[-1])
        self.assertTrue(con.is_valid_item(item_100))

if __name__ == '__main__':
    unittest.main()
