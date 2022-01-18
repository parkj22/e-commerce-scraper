
"""
product_info.py

Provides a dataclass 'Product' as a way to store
extracted data from the web and to access them easily

# Author: Jinyoung Park (parkj22)
# Version: January 19, 2022
"""

from dataclasses import dataclass, field


@dataclass
class Product:
    """
    Product currently contains five self-explanatory components:
        name, price, rating, num_reviews, link

    These components are given default values to indicate that the
    value could not be detected on the web
    """

    name: str = field(default="")
    price: float = field(default=None)
    rating: float = field(default=None)
    num_review: int = field(default=None)  # number of reviews on the product
    link: str = field(default="")  # link to the page of the product

    def to_list(self):
        """
        Returns: components in the form of a list

        to_list() is used in data organizer for passing Products
        into csv files
        """
        return [self.name, self.price, self.rating, self.num_review, self.link]

    @staticmethod
    def get_description():
        """
        Returns: Descriptions of each component in the form of a list
        """
        return ["Name", "Price", "Rating", "Number of reviews", "Link to page"]
