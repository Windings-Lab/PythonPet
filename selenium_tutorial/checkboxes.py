from selenium_loader import open_link, get_driver, WebElement

link_name = "https://the-internet.herokuapp.com/checkboxes"


def check(checkbox: WebElement, value: bool):
    if value:
        if not checkbox.is_selected():
            checkbox.click()
    else:
        if checkbox.is_selected():
            checkbox.click()


def checkbox_test(first: bool, second: bool):
    from selenium.webdriver.common.by import By

    open_link(link_name, (By.ID, "checkboxes"))

    checkboxes = get_driver().find_elements(by=By.CSS_SELECTOR, value="input[type='checkbox']")

    checkbox_id = 0
    for checkbox in checkboxes:
        checkbox_id += 1
        if checkbox_id == 1:
            check(checkbox, first)
        elif checkbox_id == 2:
            check(checkbox, second)
