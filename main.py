from init import open_link
from init import driver
from init import By

link = open_link("https://the-internet.herokuapp.com/checkboxes")

checkboxes = driver.find_elements(by=By.CSS_SELECTOR, value="input[type='checkbox']")
checkbox_id = 0
for checkbox in checkboxes:
    checkbox_id += 1
    checkbox.click()

input(driver.title)
driver.quit()
