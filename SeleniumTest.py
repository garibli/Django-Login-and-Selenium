import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
def test_successful_login():
    driver.get("http://127.0.0.1:3000/login") 
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    username_input.send_keys("fatih")
    password_input.send_keys("123456")
    submit_button.click()
    time.sleep(2)
    assert "MFA Web" in driver.page_source

def test_unsuccessful_login():
    driver.get("http://127.0.0.1:3000/login")
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    username_input.send_keys("fuad")
    password_input.send_keys("12345")
    submit_button.click()

    time.sleep(2)
    assert "Invalid Username or Password!" in driver.page_source
test_successful_login()
test_unsuccessful_login()

driver.quit()
