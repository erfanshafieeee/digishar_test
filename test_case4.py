from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
sleep(5)


product = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')
product.click()
sleep(5)


add_to_cart_button = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a')
add_to_cart_button.click()
sleep(2)
alert = Alert(driver)
alert.accept()


cart = driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[4]/a')
cart.click()
sleep(5)

delete_button = driver.find_element(By.XPATH, "//a[text()='Delete']")
delete_button.click()
sleep(2)


if "Samsung galaxy s6" not in driver.page_source:
    print("Test Passed: Product deleted successfully")
else:
    print("Test Failed: Product not deleted")

driver.quit()