from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
sleep(5)


login_cases = [
    {"username": "digishahree", "password": "123456"},  
    {"username": "erfansh", "password": "654321"},   
    {"username": "erfanshafiee", "password": "123456"}  
]


login_button = driver.find_element(By.ID, "login2")
login_button.click()
sleep(2)
for case in login_cases:
    username_field = driver.find_element(By.ID, "loginusername")
    password_field = driver.find_element(By.ID, "loginpassword")
    username_field.clear()
    password_field.clear()
    username_field.send_keys(case["username"])
    password_field.send_keys(case["password"])

    confirm_button = driver.find_element(By.XPATH, "//button[text()='Log in']")
    confirm_button.click()
    sleep(2)
    try:
        alert = driver.switch_to.alert
        alert_message = alert.text
        if "User does not exist." in alert_message or "Wrong password." in alert_message:
            print(f"Test Failed: Unexpected message for user '{case['username']}': {alert_message}")
        alert.accept()
    except:
        sleep(5)
        if f"Welcome {case['username']}" in driver.page_source:
            print(f"Test Passed: Login successful for user '{case['username']}'")
        else:
            print(f"Test Failed: Unexpected behavior for user '{case['username']}'")

driver.quit()
