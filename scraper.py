import requests
from bs4 import BeautifulSoup
from mycalendar import Calendar

class Scraper:
    def __init__(self, url) -> None:
        self.URL = url
        self.date = Calendar().date
    
    def make_soup(self):
        response = requests.get(self.URL, timeout=10)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.text, "lxml")
    

    def get_info(self):
        soup = self.make_soup()
        days = soup.select(selector="tr")
        for day in days:
            if day.strong.text == self.date:
                return day.find_all("td")