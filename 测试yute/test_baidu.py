# import pytest
# from selenium import webdriver
# class TestBaidu:
#     @pytest.fixture(autouse=True)
#     def classSetUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(5)
#     def test_title(self):
#         self.driver.get("http://www.baidu.com")
#         assert "百度一下" in self.driver.title
#     def test_logo(self):
#         pass
import fitz
print(fitz.__doc__)