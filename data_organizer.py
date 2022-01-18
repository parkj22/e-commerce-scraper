"""
data_organizer.py

Calls on data scraping modules to receive collections
of products and organize them into a csv file

# Author: Jinyoung Park (parkj22)
# Version: January 19, 2022
"""

from chrome_driver import ChromeDriver
import data_scraper_amazon
import data_scraper_ebay
import data_scraper_target
import csv
from product_info import Product


def organize():
    """
    organize() creates a csv file and
    """

    filename = "scraped-products.csv"
    f = open(filename, "w", encoding="utf8", newline="")
    writer = csv.writer(f)

    # Input the table header ["Website", "Name", ... , "Link"]
    writer.writerow(["Website"] + Product.get_description())

    # extract_to_csv(writer, "Amazon", data_scraper_amazon.extract)
    # extract_to_csv(writer, "Ebay", data_scraper_ebay.extract)
    extract_to_csv(writer, "Walmart", data_scraper_target.extract)

    # Quit browser after collecting all data
    ChromeDriver.get_instance().quit()


def extract_to_csv(writer, website_str, extract):
    products = extract()
    for product in products:
        writer.writerow([website_str] + product.to_list())
