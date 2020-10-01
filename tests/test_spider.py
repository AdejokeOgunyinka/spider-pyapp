import unittest
from src.spider import web_scraper
from src.db import DB
from src.db.pages import Pages


class TestSpider(unittest.TestCase):
    """This test class tests all the methods in the web_scraper class in the spider.py file"""

    def test_web_scraper_with_correct_value(self):
        # Test the web scraper with the correct value
        self.assertIsNone(web_scraper(1))

    def test_web_scraper_with_wrong_value(self):
        # Test the scraper with the wrong integer
        with self.assertRaises(TypeError):
            self.assertIsNone(web_scraper(3))

    def test_web_scraper_with_non_integer(self):
        # Test the scraper with non-integer
        with self.assertRaises(TypeError):
            self.assertIsNone(web_scraper('mimi'))


if __name__ == '__main__':
    unittest.main()
