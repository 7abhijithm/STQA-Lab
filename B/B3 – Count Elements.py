from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.svyasa.edu.in")

images = driver.find_elements(By.TAG_NAME,"img")
inputs = driver.find_elements(By.TAG_NAME,"input")

print("Images :",len(images))
print("Input Fields :",len(inputs))

driver.quit()