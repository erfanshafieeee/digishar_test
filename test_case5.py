from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/test")


if "404" in driver.page_source:
    print("404 error page displayed")
    try:
        back_button = driver.find_element(By.XPATH, "//a[text()='Back to store']")
        print("Test Passed: Back to store button is displayed.")
    except:
        print("Test Failed: Back to store button is not displayed.")
else:
    print("404 error page not displayed")

sleep(5)


driver.quit()
