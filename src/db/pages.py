class Pages:
    """This class implements all the functions that can be performed on the Pages table in the database"""
    def __init__(self, conn):
        # create a cursor attribute based on the connection accepted by the class
        self.cursor = conn.cursor()

    def select(self):
        # select all the data from the pages table
        self.cursor.execute('SELECT * FROM pages')
        return self.cursor.fetchall()

    def select_id(self):
        # select id from pages table in the database
        self.cursor.execute('SELECT id FROM pages')
        return self.cursor.fetchall()

    def select_url(self, page_id):
        # select all urls from the pages table in the database
        self.cursor.execute('SELECT url FROM pages where id = %s', (page_id,))
        result = self.cursor.fetchall()
        return result[0][0]

    def find(self, id_num):
        # find data in Pages table in the database, based on the id input
        self.cursor.execute('SELECT * FROM pages WHERE id = %s', (id_num,))
        return self.cursor.fetchone()

    def find_url(self, id_num):
        # find url in Pages table in the database, based on the id input
        self.cursor.execute('SELECT id,url FROM pages WHERE id = %s', (id_num,))
        result = self.cursor.fetchone()
        return result

    def update(self, value, id_num):
        # update table row in Pages table in the database, based on the id input
        self.cursor.execute('UPDATE pages SET is_scraping = %s WHERE id = %s', (value, id_num))

    def delete(self, id_num):
        # delete table row from Pages table in the database, based on the id input
        self.cursor.execute('DELETE FROM pages WHERE id = %s', (id_num,))
