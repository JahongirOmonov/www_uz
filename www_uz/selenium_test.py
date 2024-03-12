import unittest
import requests
from django.http import HttpRequest
from selenium import webdriver
from django.test import TestCase


class NewVisitorsTest(unittest.TestCase):


    def setUp(self):
        self.browser = webdriver.Chrome()



    def tearDown(self):
        print('bye')
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        self.browser.get("https://toshkent-parfum.uz")
        self.browser.save_screenshot("myscreen.png")
        self.assertIn("Toshkent parfum", self.browser.title)


if __name__ == "__main__":
    unittest.main()
