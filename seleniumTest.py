from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:5000")

print("Page title:", driver.title)

driver.quit()
