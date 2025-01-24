from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
time.sleep(5)


product = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')
product.click()
time.sleep(5)


add_to_cart_button = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a')
add_to_cart_button.click()
time.sleep(5)

alert = Alert(driver)
if "Product added" in alert.text:
    print("Test Passed: Product added successfully")
else:
    print("Test Failed: No confirmation message")

alert.accept()
driver.quit()
