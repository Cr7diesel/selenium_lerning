import os
import time
from django.test import LiveServerTestCase
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By


load_dotenv()


# class PageTests(LiveServerTestCase):
#
#     def test_admin_site(self):
#         url = 'http://127.0.0.1:8000/'
#         self.driver = webdriver.Chrome()
#         self.driver.get(url=url)
#         time.sleep(5)
#         # self.driver.get_screenshot_as_file('1.png')
#         assert 'The install worked successfully! Congratulations!' in self.driver.title


class LoginFormTest(LiveServerTestCase):
    def test_form(self):
        url = 'http://127.0.0.1:8000/admin/login/'
        self.driver = webdriver.Chrome()
        self.driver.get(url=url)
        user_name = self.driver.find_element(By.NAME, 'username')
        user_password = self.driver.find_element(By.NAME, 'password')
        time.sleep(3)
        submit = self.driver.find_element(By.CLASS_NAME, 'submit-row')
        user_name.send_keys(os.getenv('LOGIN'))
        user_password.send_keys(os.getenv('PASSWORD'))
        submit.click()
        self.driver.get_screenshot_as_file('logIn.png')
        assert 'admin' in self.driver.page_source

