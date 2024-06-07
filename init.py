from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Optional

PATH = "chromedriver.exe"

service = Service(PATH)
driver = webdriver.Chrome(service=service)

opened_link_name: str = ""


def open_link(link_name: str, locator: Optional[tuple[str, str]] = None):
    global opened_link_name
    if opened_link_name == "" or opened_link_name != link_name:
        driver.get(link_name)

    if not locator:
        return None

    by, element_name = locator
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((by, element_name))
    )
    return element
