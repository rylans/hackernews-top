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
    def test_get_item(self):
        """
        Test item retrieval and 'by' field
        """
        con = ApiConnector()
        item = con.get_item(8863)
        byline = item.get('by')
        self.assertEqual(byline, 'dhouston')
