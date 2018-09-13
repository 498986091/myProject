#encoding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver_win32\chromedriver.exe")
driver.get("http://www.sogou.com")
driver.find_element_by_id("query").clear()
driver.find_element_by_id("query").send_keys(u"广告")
driver.find_element_by_id("stb").click()
time.sleep(3)
driver.quit()