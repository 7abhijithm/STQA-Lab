from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)
error = driver.find_element(By.ID, "flash").text
print("Error Message:", error)
driver.quit()
