from bs4 import BeautifulSoup
import requests
from src.db.links import Links
from src.db import DB
from src.db.pages import Pages


def web_scraper(page_id):
    """This function accepts the id,checks if it is within the list of ids in the database, and
    scrapes only 10 links on that particular link page"""
    all_ids = Pages(DB.connect()).select_id()
    new_all_id = [pid[0] for pid in all_ids]

    if page_id not in new_all_id:
        raise TypeError('Id does not exist.')

    else:
        url = Pages(DB.connect()).select_url(page_id)
        DB.pages().update(True, page_id)
        value = requests.get(url)
        soup = BeautifulSoup(value.text, 'html.parser')

        list_urls = []
        for link in soup.find_all('a', href=True):
          if link['href'].startswith('https'):
            list_urls.append(link['href'])

        new_list_urls = list_urls[:10]
        DB.links().delete_by_page_id(page_id)

        for item in new_list_urls:
            Links(DB.connect()).insert(page_id, item)

        DB.pages().update(False, page_id)
