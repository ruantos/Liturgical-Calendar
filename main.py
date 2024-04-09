import os
from scraper import Scraper
from mycalendar import Calendar
from deliver import Deliver

URL = "https://salvemaria.com.br/calendario"
FROM_USER = os.environ.get("LOGIN")
FROM_PASSWORD = os.environ.get("PASSWORD")
TO_USER = os.environ.get("TO_USER")

scraper = Scraper(url=URL)
deliver = Deliver(FROM_USER, FROM_PASSWORD, TO_USER)

info = scraper.get_info()
msg = deliver.create_message(info)
deliver.send_email(msg)