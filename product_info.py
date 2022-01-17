"""
product_info.py

# Author: Jinyoung Park (parkj22)
# Version: January 17, 2022
"""

from dataclasses import dataclass, field


@dataclass
class Product:
    name: str = field(default="")
    price: float = field(default=None)
    rating: float = field(default=None)
    num_review: int = field(default=None)
    link: str = field(default="")
