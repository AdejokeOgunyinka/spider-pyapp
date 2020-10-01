import unittest
from src.db.pages import Pages
from src.db import DB


class TestPages(unittest.TestCase):
    """This class tests all the methods in pages.py"""
    def setUp(self) -> None:
        # set up the Pages class
        self.exec = Pages(DB.connect())

    def test_select(self):
        #  Test the select method of Pages class in pages.py
        result = self.exec.select()
        self.assertIsNotNone(result)

    def test_select_id(self):
        self.assertIsNotNone(self.exec.select_id())

    def test_select_url(self):
        # Test the select_url method of Pages class in pages.py
        self.assertIsNotNone(self.exec.select_url(1))

    def test_find(self):
        # Test the find method of Pages class in pages.py
        DB.seed()
        result = self.exec.find(2)
        self.assertIsNotNone(result)

    def test_find_url(self):
        # Test the find_url method of Pages class in pages.py
        DB.seed()
        self.assertIsNotNone(self.exec.find_url(1))

    def test_update(self):
        # Test the update method of Pages class in pages.py
        DB.seed()
        self.assertIsNone(self.exec.update(False, 1))

    def test_delete(self):
        # Test the delete method of Pages class in pages.py
        self.assertIsNone(self.exec.delete(2))

    def tearDown(self) -> None:
        # Tear down the Pages class after all tests
        self.exec = None


if __name__ == '__main__':
    unittest.main()
