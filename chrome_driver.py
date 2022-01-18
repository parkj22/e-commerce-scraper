"""
chrome_driver.py

Provides ChromeDriver for other modules to have access Selenium
WebDriver (Chrome) and browse the web

# Author: Jinyoung Park (parkj22)
# Version: January 19, 2022
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriver:
    """
    ChromeDriver holds an instance of Selenium WebDriver (Chrome)
    to be used in other modules, while restricting the instantiation
    of WebDrivers to one object at a time
    """

    __instance = None

    @staticmethod
    def get_instance():
        """
        Returns: the WebDriver instance

        get_instance() calls the constructor if the instance has not
        been initialized yet
        """
        if ChromeDriver.__instance is None:
            ChromeDriver()
        return ChromeDriver.__instance

    def __new__(cls):
        """
        __new__() initializes the instance with chrome_options, which
        is configured beforehand
        """

        # Configure chrome options here
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = True  # Setting headless true allows Chrome to run in background

        ChromeDriver.__instance = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                                   options=chrome_options)
