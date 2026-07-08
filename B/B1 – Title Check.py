from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.svyasa.edu.in")

print(driver.title)

driver.quit()