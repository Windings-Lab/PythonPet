from init import driver
from TestCases.checkboxes import checkbox_test

checkbox_test(True, False)

input(driver.title)
driver.quit()
