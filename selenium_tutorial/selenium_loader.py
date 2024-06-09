from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import Optional

PATH = "chromedriver.exe"
opened_link_name: str = ""
_driver_instance = None


def get_driver():
    global _driver_instance
    if _driver_instance is None:
        service = Service(PATH)
        _driver_instance = webdriver.Chrome(service=service)
    return _driver_instance


def open_link(link_name: str, locator: Optional[tuple[str, str]] = None):
    global opened_link_name
    if opened_link_name == "" or opened_link_name != link_name:
        get_driver().get(link_name)

    if not locator:
        return None

    by, element_name = locator
    element: WebElement = WebDriverWait(get_driver(), 10).until(
        EC.presence_of_element_located((by, element_name))
    )
    return element
