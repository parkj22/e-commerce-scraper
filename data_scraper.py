"""
data_scraper.py

# Author: Jinyoung Park (parkj22)
# Version: January 17, 2022
"""

import requests
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

import chrome_user_agent
from chrome_driver import ChromeDriver
from selenium.webdriver.common.by import By
from product_info import Product


def run():
    """
    run()
    """

    """
    
    Scraping data from Amazon:
    find all By.CLASS_NAME, "a-section.a-spacing-none"
        (name) By.CLASS_NAME, "a-size-medium.a-color-base.a-text-normal"
        (price) By.CLASS_NAME, "a-price-whole" + "a-price-fraction"
        (rating) By.CLASS_NAME, "a-section.a-spacing-none.a-spacing-top-micro" -> By.TAG_NAME, "span"
                 -> get_attribute("aria-label") -> substring [:3]
        (num_review) By.CLASS_NAME, "a-size-base"
        (link) By.CLASS_NAME, "a-link-normal.s-link-style.a-text-normal" -> ["href"]
        
    """

    browser = ChromeDriver.get_instance()
    url = "https://www.amazon.com/s?k=laptop&crid=7WTKZIVFFOXP&sprefix=laptop%2Caps%2C426&ref=nb_sb_noss_1"
    browser.get(url)

    amazon_products = []
    amazon_sections = browser.find_elements(By.CLASS_NAME, "s-result-item.s-asin.sg-col-0-of-12.sg-col-16-of-20.sg"
                                                           "-col.s-widget-spacing-small.sg-col-12-of-16")
    for section in amazon_sections:

        current_product = Product()

        name_element = section.find_elements(By.CLASS_NAME, "a-size-medium.a-color-base.a-text-normal")
        if len(name_element) > 0:
            current_product.name = name_element[0].text

        price_element_whole = section.find_elements(By.CLASS_NAME, "a-price-whole")
        price_element_fraction = section.find_elements(By.CLASS_NAME, "a-price-fraction")
        if len(price_element_whole) > 0 and len(price_element_fraction) > 0:
            current_product.price = price_element_whole[0].text + "." + price_element_fraction[0].text

        rating_element = section.find_elements(By.CLASS_NAME, "a-section.a-spacing-none.a-spacing-top-micro")
        if len(rating_element) > 0:
            rating_element = rating_element[0].find_elements(By.TAG_NAME, "span")
        if len(rating_element) > 0:
            rating_string = rating_element[0].get_attribute("aria-label")
            if rating_string is not None:
                current_product.rating = rating_string[:3]

        num_review_element = section.find_elements(By.CLASS_NAME, "a-size-base")
        if len(num_review_element) > 0 and current_product.rating is not None:
            current_product.num_review = num_review_element[0].text

        link_element = section.find_elements(By.CLASS_NAME, "a-link-normal.s-link-style.a-text-normal")
        if len(link_element) > 0:
            link_string = link_element[0].get_attribute("href")
            if link_string is not None:
                current_product.link = link_string

        print(current_product)