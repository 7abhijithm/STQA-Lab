from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.samsung.com")

links = driver.find_elements(By.TAG_NAME,"a")

buttons = driver.find_elements(By.TAG_NAME,"button")

print("Links =",len(links))

print("Buttons =",len(buttons))

driver.quit()