# data_scraper.py
# This file gathers world news from r/worldnews by using python requests library

# Author: Jinyoung Park
# Version: 1.0

import requests
from bs4 import BeautifulSoup


# scrapes data from web
def run():
    url = "https://www.reddit.com/r/worldnews/"
    res = requests.get(url)

    # Check for valid connection
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    headers = soup.find("h3", attrs={"class": ""})

    print(headers)
