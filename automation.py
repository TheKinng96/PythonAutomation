from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from model import user as user, website as web

# Defined driver and file
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
f = open('./text.txt', 'w', encoding='utf-8')

def log(message):
  f.write(message)
  f.write('\n')

def getButtonAndClick(title):
  value = "//a[contains(@href, '/{}')]".format(title)
  button = driver.find_element(By.XPATH, value=value)
  button.send_keys(Keys.RETURN)

driver.get(web["url"])
assert web["title"] in driver.title
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

# Go to Campaign page
driver.get(web["campaignPage"])
log("Got in campaign page")