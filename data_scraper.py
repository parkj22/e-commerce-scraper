"""
data_scraper.py

# Author: Jinyoung Park (parkj22)
# Version: January 13, 2022
"""

import requests
from bs4 import BeautifulSoup
import chrome_user_agent
import chrome_driver


def run():
    """
    run()
    """

    """ Accessing by BeautifulSoup
    url = "https://www.naver.com"
    headers = {
        "User-Agent": chrome_user_agent.get_user_agent()
    }

    res = requests.get(url, headers=headers)

    # Check for valid connection
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    items = soup.find_all("span", attrs={"class": "a-size-medium a-color-base a-text-normal"})
    print(items)
    """

    browser = chrome_driver.ChromeDriver.get_instance()
    url = "https://www.amazon.com/s?k=laptop"

    browser.get(url)
    browser.implicitly_wait(5)
    print(browser.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/div[2]/div[2]/div/div/div[1]/h2/a/span').text)

