import unittest
from selenium import webdriver
from Pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie testu") #preconditions
        self.driver = webdriver.Chrome()
        self.driver.get("https://bazarpupila.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.home_page = HomePage(self.driver)

        #Headless option
        # chrome_options = Options()
        # chrome_options.add_argument("--window-size=1920,1080")
        # chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("--headless")
        # self.driver = webdriver.Chrome(options=chrome_options)
    def tearDown(self):
        print("Zakonczenie testu")
        self.driver.quit()