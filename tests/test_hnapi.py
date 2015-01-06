"""
Tests
"""
from __future__ import unicode_literals

import unittest

from hnapi.connectors.api_connector import ApiConnector

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

if __name__ == '__main__':
    unittest.main()
