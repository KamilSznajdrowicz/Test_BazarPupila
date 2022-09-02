from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from Pages.base_page import BasePage
from locators import ContactFormPageLocators


class ContactForm(BasePage):
    def scroll_action(self):
        scroll = self.driver.find_element(*ContactFormPageLocators.scroll_act)
        scroll.location_once_scrolled_into_view

    def choose_salut(self, sex):
        choose_salut = Select(self.driver.find_element(*ContactFormPageLocators.choose_salut_input))
        if sex == "male":
            choose_salut.select_by_value("cec1ad09859948e1912aeaedb32fba2d")
        elif sex == "female":
            choose_salut.select_by_value("15906feb0e4d479daee9a8fb4265853b")
        else:
            choose_salut.select_by_value("224b360601394077af7997bb3ead19c4")

    def enter_name(self, name):
        name_input = self.driver.find_element(*ContactFormPageLocators.name_input)
        name_input.send_keys(name)

    def enter_surname(self, surname):
        surname_input = self.driver.find_element(*ContactFormPageLocators.surname_input)
        surname_input.send_keys(surname)

    def enter_email(self,email):
        email_input = self.driver.find_element(*ContactFormPageLocators.email_input)
        email_input.send_keys(email)

    def enter_phonenumber(self, phone_number):    # 10. Wpisz nr telefonu komórkowego
        phone_number_input = self.driver.find_element(*ContactFormPageLocators.phone_number_input)
        phone_number_input.send_keys(phone_number)

    def enter_comment(self, comment):
        comment_input = self.driver.find_element(*ContactFormPageLocators.comment_input)
        comment_input.send_keys(comment)
        subject_input = self.driver.find_element(*ContactFormPageLocators.subject_input)
        subject_input.location_once_scrolled_into_view

    def policy_click(self):
        policy_input = self.driver.find_element(*ContactFormPageLocators.policy_input)
        actions1 = ActionChains(self.driver)
        actions1.move_to_element(policy_input).perform()
        self.driver.execute_script("arguments[0].click();", policy_input)

    def send_click(self):
        send_button = self.driver.find_element(*ContactFormPageLocators.send_button)
        send_button.click()

    def report_no_title(self):
        subject_in = self.driver.find_element(*ContactFormPageLocators.subject_input)
        error_fact = (subject_in.get_attribute("validationMessage"))
        return error_fact

