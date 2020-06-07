from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# print('Selenium Easy Demo' in chrome_browser.title)
# asset 'Selenium Easy Demo' in chrome_browser.title

button = chrome_browser.find_element_by_class_name('btn-default')
# print(button_text.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

message_input = chrome_browser.find_element_by_id("user-message")
message_input.clear()
message_input.send_keys('Hey yo~')
button.click()

output_message = chrome_browser.find_element_by_id('display')
assert 'Hey yo~' in output_message.text

chrome_browser.close()