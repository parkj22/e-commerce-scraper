from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriver:
    __instance = None

    @staticmethod
    def get_instance():
        if ChromeDriver.__instance is None:
            ChromeDriver()
        return ChromeDriver.__instance

    def __new__(cls):
        if ChromeDriver.__instance is None:
            # Configure chrome options here
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.headless = True

            ChromeDriver.__instance = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                                       options=chrome_options)


def get_chrome_driver():
    """
    Returns: Configured web driver

    set_chrome_driver() uses ChromeDriverManager to install and create a chrome driver
    options.headless flag is set to true to run things in background
    """

    # Configure chrome options here
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True

    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
