import psycopg2
from decouple import config
from src.db import pages
from src.db import links


class DB:
    """This class contains methods that perform all the functions that can be performed on a database"""
    @classmethod
    def connection_details(cls):
        # Function for connecting to the database without the database name
        connection = psycopg2.connect(
          host=config('DB_HOST'),
          user=config('DB_USER'),
          password=config('DB_PASSWORD'),
          database=None)

        connection.autocommit = True
        cursor = connection.cursor()

        cursor.execute('DROP DATABASE IF EXISTS spider;')
        cursor.execute('CREATE DATABASE spider;')

        return connection

    @classmethod
    def connect(cls):
        # Connect to the database
        # Return the connection object
        try:
            new_connect = psycopg2.connect(
              host=config('DB_HOST'),
              user=config('DB_USER'),
              database=config('DB_NAME'),
              password=config('DB_PASSWORD'))

            new_connect.autocommit = True
            return new_connect

        except Exception as error:
            print(error)

    @classmethod
    def setup(cls):
        # Execute the structure SQL script
        # Return value does not matter
        cursor = cls.connect().cursor()

        with open('src/schemas/structure.sql', 'r') as file:
            string = file.readlines()
            for line in string:
                cursor.execute(line)

    @classmethod
    def seed(cls):
        # Execute the seed SQL script
        # Return value does not matter
        cls.setup()
        cursor = cls.connect().cursor()

        with open('src/schemas/seed.sql', 'r') as file:
            string = file.readlines()
            for line in string:
                cursor.execute(line)

    @classmethod
    def links(cls):
        # Returns a reference to the links interface
        return links.Links(cls.connect())

    @classmethod
    def pages(cls):
        # Returns a reference to the pages interface
        return pages.Pages(cls.connect())
