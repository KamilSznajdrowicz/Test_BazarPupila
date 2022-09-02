from Pages.base_page import BasePage
from locators import HomePageLocators


class HomePage(BasePage):
    def click_account(self):
        my_account = self.driver.find_element(*HomePageLocators.my_account_btn)
        my_account.click()

    def click_sign_in(self):
        sign_in = self.driver.find_element(*HomePageLocators.sign_in_btn)
        sign_in.click()

    def click_contact(self):
        contact = self.driver.find_element(*HomePageLocators.contact_side_btn)
        contact.click()