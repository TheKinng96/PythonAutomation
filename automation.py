from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from model import user

# Defined driver and file
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
f = open('./text.txt', 'w')

def log(message):
  f.write(message)
  f.write('\n')

driver.get(user["website"])
assert "アドシスト" in driver.title
message = 'Accessed website: ' + driver.title + ' at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
log(message)

# Login
emailField = driver.find_element(By.ID, value='loginEmail')
emailField.clear()
emailField.send_keys(user["email"])
passwordField = driver.find_element(By.ID, value='loginPassword')
passwordField.clear()
passwordField.send_keys(user["password"])
buttonLogin = driver.find_element(By.ID, value='buttonLogin')
buttonLogin.send_keys(Keys.RETURN)
message = "Logined successfully as " + user["email"]
log(message)

# emailField = driver.find_element(By.ID, 'loginEmail')
# emailField.send_keys('wordpress-ec@test.com')
# passwordField = driver.find_element('loginPassword')
# passwordField.send_keys('password')

# button = driver.find_element_by_class_name('btn-default')
# # print(button_text.get_attribute('innerHTML'))

# assert 'Show Message' in driver.page_source

# message_input = driver.find_element_by_id("user-message")
# message_input.clear()
# message_input.send_keys('Hey yo~')
# button.click()

# output_message = driver.find_element_by_id('display')
# assert 'Hey yo~' in output_message.text

# driver.close()