
"""
data_organizer.py

This module passes on given inputs to modules that scrapes websites
specified by the user and collects all returned information on 'scraped-products.csv'

# Author: Jinyoung Park (parkj22)
# Version: January 22, 2022
"""

import data_scraper_etsy
import search_window
import data_scraper_amazon
import data_scraper_ebay
import csv
from chrome_driver import ChromeDriver
from product_info import Product


def organize(search, path, amazon, ebay, etsy, num_page):
    """
    organize(): handles user's input from the Tk window and passes
    'search' and 'num_page' to appropriate scraper modules.
    search: URL query parameter
    path: directory path for the csv file 'scraped-products.csv'
    amazon: boolean value for scraping on Amazon.com
    ebay: boolean value for scraping on Ebay.com
    etsy: boolean value for scraping on Etsy.com
    num_page: total number of pages to be scraped
    """

    # csv file is created at the path given by the user
    filename = path + "/scraped-products.csv"
    f = open(filename, "w", encoding="utf8", newline="")
    writer = csv.writer(f)

    # Input the table header ["Website", "Name", ... , "Link"]
    writer.writerow(["Website"] + Product.get_description())

    # Pass on 'search' and 'num_page' to modules specified by the user
    if amazon:
        extract_to_csv(writer, "Amazon", data_scraper_amazon.extract, search, num_page)
    if ebay:
        extract_to_csv(writer, "Ebay", data_scraper_ebay.extract, search, num_page)
    if etsy:
        extract_to_csv(writer, "Etsy", data_scraper_etsy.extract, search, num_page)

    # Info message is popped up when collecting / writing data is complete
    search_window.notify_complete()


def extract_to_csv(writer, website_str, extract, search, num_page):
    """
    extract_to_csv(): writes returned information to the csv file
    writer: csv writer object
    website_str: Name of the website which the information is from
    extract: scraping function from modules
    search: URL query parameter
    num_page: total number of pages to be scraped
    """
    products = extract(search, num_page)
    for product in products:
        writer.writerow([website_str] + product.to_list())
