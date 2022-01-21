
"""
data_scraper_ebay.py

Scrapes information about products on Ebay.com

# Author: Jinyoung Park (parkj22)
# Version: January 22, 2022
"""

import search_window
from chrome_driver import ChromeDriver
from selenium.webdriver.common.by import By
from product_info import Product


def extract(search, num_page):
    """
    Returns: a list of products and their information found
    on Ebay.com

    extract() browses through webpages and scrapes
    various types of data to create a collection of products
    search: URL query parameter
    num_page: total number of pages to be scraped
    """

    browser = ChromeDriver.get_instance()
    ebay_products = []  # Will be collecting all products here

    # Iterate as many pages as required
    for i in range(1, num_page + 1):
        # Set url to each page and browse
        url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw={}&_sacat=0&_pgn={}".format(search, i)
        browser.get(url)

        # Update progress frame to hint what webpage is being scraped
        search_window.progress_frame.configure(text="Ebay (Page {}/{})".format(i, num_page))
        search_window.progress_frame.update()

        # Locate all sections for each product and configure progress bar accordingly
        ebay_sections = browser.find_elements(By.CLASS_NAME, "s-item__info.clearfix")
        search_window.progress.configure(maximum=len(ebay_sections))
        index = 1

        # Iterate through all sections to extract needed values
        for section in ebay_sections:
            # Initialize an empty Product
            current_product = Product()

            # Extract values here
            extract_name(section, current_product)
            extract_price(section, current_product)
            extract_rating(section, current_product)
            extract_num_review(section, current_product)
            extract_link(section, current_product)

            # Add to the final collection
            if current_product.name != "":
                ebay_products.append(current_product)

            # Update progress bar
            search_window.progress_var.set(index)
            search_window.progress.update()
            index += 1

    search_window.progress.stop()
    return ebay_products


def extract_name(section, product):
    """
    extract_name() finds the product's name in the section
    and modifies the name in 'product'

    Note: find_elements() is used in place of find_element()
    in order to save unnecessary try/catch blocks. This pattern
    occurs in other extract functions for the same purpose
    """
    # Locate the element that contains the name
    elements = section.find_elements(By.CLASS_NAME, "s-item__title")

    # Equivalent to 'if the element exist'
    if len(elements) > 0:
        product.name = elements[0].text


def extract_price(section, product):
    """
    extract_price() finds the product's price in the section
    and modifies the price in 'product'
    """
    # Locate the element that contains the price
    elements = section.find_elements(By.CLASS_NAME, "s-item__price")

    # Equivalent to 'if the element exist'
    if len(elements) > 0:
        product.price = elements[0].text.replace("$", "")


def extract_rating(section, product):
    """
    extract_rating() finds the product's rating in the section
    and modifies the rating in 'product'
    """
    # Locate element for rating
    elements = section.find_elements(By.CLASS_NAME, "x-star-rating")
    if len(elements) > 0:
        elements = elements[0].find_elements(By.CLASS_NAME, "clipped")
    if len(elements) > 0:
        # Rating is stored in an attribute called aria-label
        product.rating = elements[0].text.replace(" out of 5 stars.", "")


def extract_num_review(section, product):
    """
    extract_num_review() finds the product's number of reviews
    in the section and modifies the num_review in 'product'
    """
    # Locate element for number of reviews
    elements = section.find_elements(By.CLASS_NAME, "s-item__reviews-count")
    if len(elements) > 0:
        elements = elements[0].find_elements(By.TAG_NAME, "span")
    if len(elements) > 0:
        product.num_review = elements[0].text.replace(" product ratings", "").replace(" product rating", "")


def extract_link(section, product):
    """
    extract_link() finds the link to the page in the section
    and modifies the link in 'product'
    """
    # Locate element for link
    elements = section.find_elements(By.CLASS_NAME, "s-item__link")
    if len(elements) > 0:
        link_str = elements[0].get_attribute("href")
        if link_str is not None:
            product.link = link_str
