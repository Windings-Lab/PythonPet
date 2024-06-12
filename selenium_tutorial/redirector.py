from selenium_loader import open_link, get_driver


link_name = "https://the-internet.herokuapp.com/redirector"


def redirector_test():
    from selenium.webdriver.common.by import By

    open_link(link_name)

    redirector_link = get_driver().find_element(By.LINK_TEXT, "here")
    redirector_link.click()
