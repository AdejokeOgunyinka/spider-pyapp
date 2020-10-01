import unittest
from src.db import DB
from src.db.links import Links


class TestLinks(unittest.TestCase):
    """This class tests all the functions in the Links class in links.py"""
    def setUp(self) -> None:
        # Set up the Links class
        self.exec = Links(DB.connect())

    def test_insert(self):
        # Test the insert method of the Links class in links.py
        DB.setup()
        DB.seed()
        self.assertIsNone(self.exec.insert(1, 'https://facebook.com'))

    def test_select(self):
        # Test the select method of the Links class in links.py
        DB.setup()
        DB.seed()
        self.assertIsNotNone(self.exec.select())

    def test_find_with_page_id(self):
        # Test the find_with_page_id method of the Links class in links.py
        self.assertIsNone(self.exec.find_with_page_id(1))

    def test_delete_by_page_id(self):
        # Test the delete_by_page_id method of the Links class in links.py
        self.assertIsNone(self.exec.delete_by_page_id(1))

    def tearDown(self) -> None:
        # Tear down the Links class after all the tests
        self.exec = None


if __name__ == '__main__':
    unittest.main()
