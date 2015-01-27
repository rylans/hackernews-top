"""
Tests
"""
from __future__ import unicode_literals

import unittest

from hnapi.connectors.api_connector import ApiConnector
from hnapi.connectors.api_connector import NetworkError

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
        self.assertTrue(con.is_api_item(item_0))

        item_100 = con.get_item(top[-1])
        self.assertTrue(con.is_api_item(item_100))

    def test_bad_api_request(self):
        """
        Test that api fails with appropriate error
        """
        con = ApiConnector()
        self.assertRaises(NetworkError, \
                con.request, "http://hacker-news.firebaseio.com/v0/foobar")

    def test_set_timeout_error(self):
        """
        Test that set_timeout throws a RuntimeError
        """
        con = ApiConnector()
        self.assertRaises(RuntimeError, con.set_timeout, -1)

    def test_set_timeout(self):
        """
        Test set_timeout
        """
        con = ApiConnector()
        con.set_timeout(4)
        self.assertEqual(con.timeout, 4)

    def test_get_kids(self):
        """
        Test retrieval of comment usernames from a story
        """
        con = ApiConnector()
        item = con.get_item(8863)
        user_dict = con.get_kids(item)
        self.assertEqual(user_dict['noisemaker'], 'noisemaker')
        self.assertEqual(user_dict['jganetsk'], 'jganetsk')
        self.assertEqual(user_dict['vlad'], 'vlad')

    def test_get_surrogate_item(self):
        """
        Test retrieval of item that isn't really an item
        """
        con = ApiConnector()
        item = con.get_item(8847790)
        self.assertTrue(con.is_valid_item(item))

        byline = item.get('by')
        self.assertEqual(byline, '')

    def test_get_poll_item(self):
        """
        Test retrieval of 'poll'
        """
        con = ApiConnector()
        item = con.get_item(7059569)
        self.assertTrue(con.is_valid_item(item))
        self.assertEqual(item.get('type'), 'poll')

    def test_is_dead_true(self):
        """
        Test that a dead item is determined to be dead
        """
        con = ApiConnector()
        item = con.get_item(8937830)
        self.assertTrue(con.is_dead_item(item))

    def test_is_dead_false(self):
        """
        Test that a non-dead item is determined to be not dead
        """
        con = ApiConnector()
        item = con.get_item(2549)
        self.assertFalse(con.is_dead_item(item))

    def test_make_item_endpoint_error(self):
        """
        Test that make_item_endpoint throws an error when it takes a
        non-integer parameter
        """
        con = ApiConnector()
        self.assertRaises(RuntimeError, con.make_item_endpoint, "asdf")

if __name__ == '__main__':
    unittest.main()
