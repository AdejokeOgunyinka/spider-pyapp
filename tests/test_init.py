import unittest
from src.db import DB


class TestUnit(unittest.TestCase):
    """This class tests all the methods in DB class in the src/db file"""
    def setUp(self) -> None:
        """Set up the connection"""
        self.exec = DB().connection_details()

    def test_connection_details(self):
        """Test the connection that was set up"""
        self.assertIsNotNone(self.exec)

    def test_connect(self):
        """Test new connection of the database"""
        self.assertIsNotNone(DB().connect())

    def test_setup(self):
        """Test the creation of the database table"""
        self.assertIsNone(DB().setup())

    def test_seed(self):
        """Test the insert of information into the database table created"""
        self.assertIsNone(DB().seed())

    def test_links(self):
        """Test the reference to the links interface"""
        self.assertIsNotNone(DB().links())

    def test_pages(self):
        """Test the reference to the pages interface"""
        self.assertIsNotNone(DB().pages())

    def tearDown(self) -> None:
        """Tear down the connection"""
        self.exec = None


if __name__ == '__main__':
    unittest.main()
