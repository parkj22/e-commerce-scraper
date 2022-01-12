"""
data_scraper.py

# Author: Jinyoung Park (parkj22)
# Version: January 13, 2022
"""

import requests
from bs4 import BeautifulSoup
import chrome_user_agent


def run():
    """
    run()
    """
    url = "https://www.amazon.com/s?k=latops"
    headers = {
        "User-Agent": chrome_user_agent.get_user_agent()
    }

    res = requests.get(url, headers=headers)

    # Check for valid connection
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    items = soup.find_all("span", attrs={"class": "a-size-medium a-color-base a-text-normal"})
    print(items)
