#encoding=utf-8
from selenium import webdriver
import unittest

class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Ie(executable_path="D:\webdriver\IEDriverServer_Win32_3.14.0\IEDriverServer.exe")
    def test_simulateASingleKeys(self):
        url = "http://www.sogou.com"
        self.driver.get(url)
        from selenium.webdriver.common.keys import Keys
        import time
        query = self.driver.find_element_by_id("query")
        query.send_keys(Keys.F12)
        time.sleep(3)
        query.send_keys(Keys.F12)
        query.send_keys("selenium")
        query.send_keys(Keys.ENTER)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()