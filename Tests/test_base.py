import unittest
from selenium import webdriver
from Pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie testu") #warunki wstepne
        self.driver = webdriver.Chrome()
        self.driver.get("https://bazarpupila.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        print("Zakonczenie testu")
        self.driver.quit()