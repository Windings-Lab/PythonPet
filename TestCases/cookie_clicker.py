from init import driver
from init import open_link
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def select_language(language_name: str) -> None:
    language = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{language_name}')]"))
    )
    language.click()


def cookie_clicker_test():
    open_link("https://orteil.dashnet.org/cookieclicker/")

    select_language("English")

    cookie_id = "bigCookie"
    WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, cookie_id))
    )

    cookie = driver.find_element(By.ID, cookie_id)
    cookie.click()

    while True:
        cookie.click()
        cookies_count = driver.find_element(By.ID, "cookies").text.split(" ")[0]
        print(cookies_count)
        if int(cookies_count) == 100:
            break
