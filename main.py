# Show examples of how you would use ALL your implementations here
from src.db import DB
from celery import Celery
from decouple import config
from src.db.pages import Pages
from src.spider import web_scraper


# DB.seed()
# DB.pages().select()
# DB.pages().find(1)
# DB.pages().find(3)
# DB.pages().update(1)
# DB.pages().update(1)
# DB.pages().delete(1)

# print(DB.pages().select())

# DB.connection_details()
# print(DB.connect())
# print(DB.setup())
# print(DB.seed())

app = Celery('spider', backend=config('CELERY_BACKEND'), broker=config('CELERY_BROKER'))


@app.task()
def task():
    return web_scraper(Pages(DB.connect()).find_url(1))
