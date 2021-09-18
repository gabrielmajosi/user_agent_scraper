import requests
from bs4 import BeautifulSoup
import logging

base_URL = "http://www.useragentstring.com/pages/useragentstring.php?name="

def scrape_agents_(browsers):
    scraped_agents = []

    for browser in browsers:
        logging.info(f"getting agents for {browser}")

        r = requests.get(f"{base_URL}{browser}")
        soup = BeautifulSoup(r.content, "html.parser")

        for tag in soup.find("div", id="liste").find_all("a"):
            for string in tag.strings:
                scraped_agents.append(string)

    return scraped_agents

def validate_browser_list_(browsers):
    logging.info("validating browser list")
    valid_browsers = []

    # do request and init soup
    r = requests.get("http://www.useragentstring.com/pages/useragentstring.php")
    soup = BeautifulSoup(r.content, "html.parser")

    # compile valid browser list
    for menu_name_object in soup.find_all("a", class_="unterMenuName"):
        for browser_name in menu_name_object.strings:
            valid_browsers.append(browser_name)

    # loop to check against valid list
    for browser in browsers:
        if browser not in valid_browsers:
            raise Exception("invalid browser; check spelling and capitilization")

    return valid_browsers

def get_valid_agents():
    return validate_browser_list_([])

def scrape_user_agents(browsers):
    validate_browser_list_(browsers)
    return scrape_agents_(browsers)


