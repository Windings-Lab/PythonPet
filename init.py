from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PATH = "chromedriver.exe"

service = Service(PATH)
driver = webdriver.Chrome(service=service)


def open_link(link):
    return driver.get(link)
