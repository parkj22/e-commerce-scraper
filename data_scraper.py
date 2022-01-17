"""
data_scraper.py

# Author: Jinyoung Park (parkj22)
# Version: January 13, 2022
"""

import requests
from bs4 import BeautifulSoup
import chrome_user_agent
import chrome_driver
from selenium.webdriver.common.by import By


def run():
    """
    run()
    """

    browser = chrome_driver.ChromeDriver.get_instance()
    url = "https://www.amazon.com/s?k=laptop&crid=7WTKZIVFFOXP&sprefix=laptop%2Caps%2C426&ref=nb_sb_noss_1"
    browser.get(url)

    amazon_product_names = browser.find_elements(By.CLASS_NAME, "a-size-medium.a-color-base.a-text-normal")

    for name in amazon_product_names:
        print(name.text)
