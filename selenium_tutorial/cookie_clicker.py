from selenium_loader import get_driver
from selenium_loader import open_link
from selenium_loader import EC
from selenium_loader import WebDriverWait

from selenium.webdriver.common.by import By


def select_language(language_name: str) -> None:
    language = WebDriverWait(get_driver(), 5).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{language_name}')]"))
    )
    language.click()


def cookie_clicker_test():
    open_link("https://orteil.dashnet.org/cookieclicker/")

    select_language("English")

    cookie_id = "bigCookie"
    WebDriverWait(get_driver(), 30).until(
            EC.presence_of_element_located((By.ID, cookie_id))
    )

    cookie = get_driver().find_element(By.ID, cookie_id)
    cookie.click()

    while True:
        cookie.click()
        cookies_count = get_driver().find_element(By.ID, "cookies").text.split(" ")[0]
        print(cookies_count)
        if int(cookies_count) == 100:
            break
