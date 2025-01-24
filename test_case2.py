from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
sleep(5)


users = [
    {"username": "testuser", "password": "testpassword"},
    {"username": "newtestuser", "password": "newtestpassword"},
    {"username": "erfanshafiee", "password": "123456"},
    {"username": "erfansh", "password": "erfan12345"}
]
signup_button = driver.find_element(By.ID, "signin2")
signup_button.click()
sleep(2)

for user in users:
    username_field = driver.find_element(By.ID, "sign-username")
    password_field = driver.find_element(By.ID, "sign-password")
    username_field.clear()
    password_field.clear()
    username_field.send_keys(user["username"])
    password_field.send_keys(user["password"])

    confirm_button = driver.find_element(By.XPATH, "//button[text()='Sign up']")
    confirm_button.click()
    sleep(2)


    try:
        alert = Alert(driver)
        alert_text = alert.text
        print("Alert message:", alert_text)

        if "This user already exist." in alert_text:
            print(f"Test Failed: User '{user['username']}' already exists.")
            alert.accept()
        elif "Sign up successful." in alert_text:
            print(f"Test Passed: User '{user['username']}' registered successfully.")
            alert.accept()
        else:
            print(f"Test Failed: Unexpected alert message for user '{user['username']}': {alert_text}")
            alert.accept()
    except Exception as e:
        print(f"No alert appeared for user '{user['username']}'. Test inconclusive.", str(e))


driver.quit()