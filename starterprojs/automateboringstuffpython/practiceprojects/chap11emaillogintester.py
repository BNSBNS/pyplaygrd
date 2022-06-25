import email
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-user')
emailElem.send_keys('notemail')
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('123')
passwordElem.submit()