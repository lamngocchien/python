from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_browser = webdriver.Chrome('chromedriver.exe')

print(chrome_browser)
chrome_browser.get("http://www.google.com.vn")
input_text = chrome_browser.find_element_by_name('q')
input_text.send_keys('Bão')

input_text.send_keys(Keys.ENTER)

