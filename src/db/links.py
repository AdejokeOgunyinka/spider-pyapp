class Links:
    """This class contains all the functions that can be performed on the links table"""
    def __init__(self, conn):
        # create a cursor attribute based on the connection accepted by the class
        self.connect = conn
        self.cursor = conn.cursor()

    def insert(self, page_id, url):
        # Insert into the links table in the database
        return self.cursor.execute('INSERT INTO links (page_id,url) VALUES (%s, %s)', (page_id, url))

    def select(self):
        # selects all from the Links table in the database
        self.cursor.execute('SELECT * FROM links')
        return self.cursor.fetchall()

    def find_with_page_id(self, page_id):
        # selects from the Links table in the database based on page_id
        return self.cursor.execute('SELECT * FROM links WHERE page_id = %s', (page_id,))

    def delete_by_page_id(self, page_id):
        # deletes from the Links table in the database based on page_id
        return self.cursor.execute('DELETE FROM links WHERE page_id = %s', (page_id,))
