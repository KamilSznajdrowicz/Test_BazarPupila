from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from Pages.base_page import BasePage
from locators import RegistrationPageLocators
from selenium.webdriver.common.by import By


class RegistrationPage(BasePage):
    def scroll_action(self):
        loginPassword_input = self.driver.find_element(By.ID, 'loginPassword')
        loginPassword_input.location_once_scrolled_into_view

    def person_input(self, type_account):
        choose_person = Select(self.driver.find_element(*RegistrationPageLocators.choose_person_btn))
        choose_person.select_by_value(type_account)

    def choose_salut(self, sex):
        choose_salut = Select(self.driver.find_element(*RegistrationPageLocators.choose_salut_btn))
        if sex == "male":
            choose_salut.select_by_value("cec1ad09859948e1912aeaedb32fba2d")
        elif sex == "female":
            choose_salut.select_by_value("15906feb0e4d479daee9a8fb4265853b")
        else:
            choose_salut.select_by_value("224b360601394077af7997bb3ead19c4")

    def enter_name(self, name):
        name_input = self.driver.find_element(*RegistrationPageLocators.name_input_in)
        name_input.send_keys(name)

    def enter_surname(self, surname):
        surname_input = self.driver.find_element(*RegistrationPageLocators.surname_input_in)
        surname_input.send_keys(surname)

    def enter_email(self,email):
        email_input = self.driver.find_element(*RegistrationPageLocators.email_input_in)
        email_input.send_keys(email)

    def enter_password(self,password):
        pass_input = self.driver.find_element(*RegistrationPageLocators.pass_input_in)
        pass_input.send_keys(password)
        pass_input.location_once_scrolled_into_view

    def enter_address(self, street):
        address_input = self.driver.find_element(*RegistrationPageLocators.address_input_in)
        address_input.send_keys(street)
        address_input.location_once_scrolled_into_view

    def enter_postcode(self, post_code):
        post_code_input = self.driver.find_element(*RegistrationPageLocators.post_code_input_in)
        post_code_input.send_keys(post_code)

    def enter_city(self, city):
        city_input = self.driver.find_element(*RegistrationPageLocators.city_input_in)
        city_input.send_keys(city)

    def enter_phonenumber(self, phone_number):
        phone_number_input = self.driver.find_element(*RegistrationPageLocators.phone_number_input_in)
        phone_number_input.send_keys(phone_number)

    def click_policy(self):
        policy_input = self.driver.find_element(*RegistrationPageLocators.policy_input)
        actions1 = ActionChains(self.driver)
        actions1.move_to_element(policy_input).perform()
        self.driver.execute_script("arguments[0].click();", policy_input)

    def click_register(self):
        register_button = self.driver.find_element(*RegistrationPageLocators.register_button_btn)
        register_button.click()

    def report_email(self):    # 13. Raport
        emailField = self.driver.find_element(*RegistrationPageLocators.email_input_in)
        error_fact = (emailField.get_attribute("validationMessage"))
        return error_fact

    def report_pass(self):
        pass_input = self.driver.find_element(*RegistrationPageLocators.pass_input_in)
        error_fact = (pass_input.get_attribute("validationMessage"))
        return error_fact

    def enter_factory(self, factory):
        factory_input = self.driver.find_element(*RegistrationPageLocators.factory_input_in)
        factory_input.send_keys(factory)

    def enter_department(self, department):
        department_input = self.driver.find_element(*RegistrationPageLocators.department_input_in)
        department_input.send_keys(department)

    def report_nip(self):
        nip = self.driver.find_element(*RegistrationPageLocators.NIP_input)
        error_fact = (nip.get_attribute("validationMessage"))
        return error_fact



