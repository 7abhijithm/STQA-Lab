from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://amazon.com")
print(driver.title)
driver.quit()