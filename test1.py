from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up driver
driver = webdriver.Chrome()

# Open the website
driver.get("https://demo.nopcommerce.com/")

# Maximize window
driver.maximize_window()

#first click ligin link
driver.find_element(By.XPATH,"//a[@class='ico-login']").click()
time.sleep(5)

#  Locate username and password fields
driver.find_element(By.CLASS_NAME, "email").send_keys("ajitpoojari03@gmail.com")
driver.find_element(By.CLASS_NAME, "password").send_keys("Aj03@890")

# Click login button
driver.find_element(By.CLASS_NAME, "button-1 login-button").click()

# Wait for page to load
time.sleep(2)

# Check if login is successful by title or page element
if "nopCommerce demo store. Home page title" in driver.title:
    print("Login Test Passed ")
else:
    print("Login Test Failed ")

# Close the browser
driver.quit()
