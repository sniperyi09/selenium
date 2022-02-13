from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("./chromedriver")

driver.get("http:\\d-seller.poomgo.com")
driver.implicitly_wait(3)

driver.find_element_by_name('username').send_keys('김유일1')
driver.find_element_by_name('password').send_keys('1q2w3e4r5t!')
driver.find_element_by_xpath('//*[@id="login-form"]/div[5]/button').click()
