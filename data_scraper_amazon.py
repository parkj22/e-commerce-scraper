
"""
data_scraper_amazon.py

Scrapes information about products on Amazon.com

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
    on Amazon.com

    extract(): browses through webpages and scrapes
    various types of data to create a collection of products
    search: URL query parameter
    num_page: total number of pages to be scraped
    """

    browser = ChromeDriver.get_instance()
    amazon_products = []  # Will be collecting all products here

    # Iterate as many pages as required
    for i in range(1, num_page + 1):
        # Set url to each page and browse
        url = "https://www.amazon.com/s?k={}&page={}".format(search, i)
        browser.get(url)

        # Update progress frame to hint what webpage is being scraped
        search_window.progress_frame.configure(text="Amazon (Page {}/{})".format(i, num_page))
        search_window.progress_frame.update()

        # Locate all sections for each product and configure progress bar accordingly
        amazon_sections = browser.find_elements(By.CLASS_NAME, "s-result-item.s-asin.sg-col-0-of-12.sg-col-16-of-20.sg"
                                                               "-col.s-widget-spacing-small.sg-col-12-of-16")
        search_window.progress.configure(maximum=len(amazon_sections))
        index = 1

        # Iterate through all sections to extract needed values
        for section in amazon_sections:
            # Initialize an empty Product
            current_product = Product()

            # Extract values here
            extract_name(section, current_product)
            extract_price(section, current_product)
            extract_rating(section, current_product)
            extract_num_review(section, current_product)
            extract_link(section, current_product)

            # Add to the final collection
            amazon_products.append(current_product)

            # Update progress bar
            search_window.progress_var.set(index)
            search_window.progress.update()
            index += 1

    search_window.progress.stop()
    return amazon_products


def extract_name(section, product):
    """
    extract_name() finds the product's name in the section
    and modifies the name in 'product'

    Note: find_elements() is used in place of find_element()
    in order to save unnecessary try/catch blocks. This pattern
    occurs in other extract functions for the same purpose
    """
    # Locate the element that contains the name
    elements = section.find_elements(By.CLASS_NAME, "a-size-medium.a-color-base.a-text-normal")

    # Equivalent to 'if the element exist'
    if len(elements) > 0:
        product.name = elements[0].text


def extract_price(section, product):
    """
    extract_price() finds the product's price in the section
    and modifies the price in 'product'

    Note: price on Amazon is divided into two separate values:
        the whole part and the fraction part (e.g. 14 and .99)
    """
    # Locate two elements that contain the price
    elements_whole = section.find_elements(By.CLASS_NAME, "a-price-whole")
    elements_fraction = section.find_elements(By.CLASS_NAME, "a-price-fraction")

    # Equivalent to 'if both elements exist'
    if len(elements_whole) > 0 and len(elements_fraction) > 0:
        # For the final price, two parts are appended with '.' in the middle
        product.price = elements_whole[0].text + "." + elements_fraction[0].text


def extract_rating(section, product):
    """
    extract_rating() finds the product's rating in the section
    and modifies the rating in 'product'
    """
    # Locate element for rating
    elements = section.find_elements(By.CLASS_NAME, "a-section.a-spacing-none.a-spacing-top-micro")
    if len(elements) > 0:
        elements = elements[0].find_elements(By.TAG_NAME, "span")
    if len(elements) > 0:
        # Rating is stored in an attribute called aria-label
        rating_str = elements[0].get_attribute("aria-label")
        if rating_str is not None:
            product.rating = rating_str.replace(" out of 5 stars", "")  # Trim the string to get float value


def extract_num_review(section, product):
    """
    extract_num_review() finds the product's number of reviews
    in the section and modifies the num_review in 'product'

    Note: extract_rating() needs to be run first, as having rating
    as None will result in no modification on num_review
    """
    # Locate element for number of reviews
    elements = section.find_elements(By.CLASS_NAME, "a-size-base")
    if len(elements) > 0 and product.rating is not None:
        product.num_review = elements[0].text


def extract_link(section, product):
    """
    extract_link() finds the link to the page in the section
    and modifies the link in 'product'
    """
    # Locate element for link
    elements = section.find_elements(By.CLASS_NAME, "a-link-normal.s-link-style.a-text-normal")
    if len(elements) > 0:
        link_str = elements[0].get_attribute("href")
        if link_str is not None:
            product.link = link_str
