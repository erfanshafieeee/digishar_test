from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
sleep(5)

login_button = driver.find_element(By.ID, "login2")
login_button.click()
sleep(2)

username_field = driver.find_element(By.ID, "loginusername")
password_field = driver.find_element(By.ID, "loginpassword")
username_field.send_keys("erfanshafiee")
password_field.send_keys("123456")

confirm_button = driver.find_element(By.XPATH, "//button[text()='Log in']")
confirm_button.click()
sleep(10)


if "Welcome erfanshafiee" in driver.page_source:
    print("Login successful.")

    logout_button = driver.find_element(By.ID, "logout2")
    logout_button.click()
    sleep(2)

    if driver.find_element(By.ID, "login2").is_displayed():
        print("Test Passed: Log out successful and Log in button is displayed.")
    else:
        print("Test Failed: Log out unsuccessful or Log in button is not displayed.")
else:
    print("Test Failed: Login was not successful. Cannot proceed with Log out test.")


driver.quit()
