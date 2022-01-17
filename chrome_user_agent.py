
"""
chrome_user_agent.py

# Author: Jinyoung Park (parkj22)
# Version: January 17, 2022
"""

from chrome_driver import ChromeDriver


def get_user_agent():
    """
    Returns: Detected User-Agent value from www.whatsmyua.info

    get_user_agent() looks into a website that provides User-Agent and extracts it from the element
    User-Agent is set from "HeadlessChrome" to "Chrome"
    """

    browser = ChromeDriver.get_instance()
    url = "https://www.whatsmyua.info"

    # Access the url and find the value
    browser.get(url)
    user_agent = browser.find_element("id", "custom-ua-string").text
    browser.quit()

    # "HeadlessChrome" is often blocked for unwanted traffic, so
    # replace it with "Chrome" instead
    user_agent = user_agent.replace("HeadlessChrome", "Chrome")

    return user_agent
