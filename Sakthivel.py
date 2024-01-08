from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://github.com/")
print("Successfully redirected")
