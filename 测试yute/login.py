import time
import unittest
import operator
from selenium import webdriver
import account
class TestLoginGmail(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("Chromedriver.exe")
        cls.driver.implicitly_wait(10)
    def test_add(self):
        self.assertEqual(operator.add(5,3),8)
    def test_login(self):
        self.driver.get('https://mail.google.com')
        time.sleep(10)
        self.driver.find_element_by_id('identifierId').send_keys(account.EMAL)
        time.sleep(10)
        self.driver.find_element_by_id('identifierNext').click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(account.PASSWORD)
        time.sleep(20)
        self.assertIn('收件箱',self.driver.title)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()
