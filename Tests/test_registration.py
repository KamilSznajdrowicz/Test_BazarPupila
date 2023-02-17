from Pages.home_page import HomePage
from Pages.registration_page import RegistrationPage
from Tests.test_base import BaseTest
from data import type_account2, sex, fakename, fakesurname, email_correct, password, street, post_code, city, phone_number, email, type_account, password_short, factory, department, facebook_email, facebook_password


class RegistrationTest(BaseTest):
    def testInCorrectEmail(self):
        hp = HomePage(self.driver)
        hp.click_account()
        hp.click_sign_in()
        rp=RegistrationPage(self.driver)
        rp.scroll_action()
        rp.person_input(type_account)
        rp.choose_salut(sex)
        rp.enter_name(fakename)
        rp.enter_surname(fakesurname)
        rp.enter_email(email)
        rp.enter_password(password)
        rp.enter_address(street)
        rp.enter_postcode(post_code)
        rp.enter_city(city)
        rp.enter_phonenumber(phone_number)
        rp.click_policy()
        rp.click_register()
        rp.report_email()
        error_expected = "Please enter a part followed by '@'. '@wp.pl' is incomplete."
        print(rp.report_email())
        self.assertEqual(rp.report_email(), error_expected)

    def testPasswordTooShort(self):
        hp = HomePage(self.driver)
        hp.click_account()
        hp.click_sign_in()
        rp = RegistrationPage(self.driver)
        rp.scroll_action()
        rp.person_input(type_account)
        rp.choose_salut(sex)
        rp.enter_name(fakename)
        rp.enter_surname(fakesurname)
        rp.enter_email(email_correct)
        rp.enter_password(password_short)
        rp.enter_address(street)
        rp.enter_postcode(post_code)
        rp.enter_city(city)
        rp.enter_phonenumber(phone_number)
        rp.click_policy()
        rp.click_register()
        rp.report_pass()
        error_expected = " Minimalna liczba znaków w haśle to 8."
        print(rp.report_pass())
        self.assertEqual(rp.report_pass(), error_expected)

    def testBusinessmanWithoutNIP(self):
        hp = HomePage(self.driver)
        hp.click_account()
        hp.click_sign_in()
        rp = RegistrationPage(self.driver)
        rp.scroll_action()
        rp.person_input(type_account2)
        rp.choose_salut(sex)
        rp.enter_name(fakename)
        rp.enter_surname(fakesurname)
        rp.enter_factory(factory)
        rp.enter_department(department)
        rp.enter_email(email_correct)
        rp.enter_password(password)
        rp.enter_address(street)
        rp.enter_postcode(post_code)
        rp.enter_city(city)
        rp.enter_phonenumber(phone_number)
        rp.click_policy()
        rp.click_register()
        rp.report_nip()
        error_expected = "Please fill out this field."
        print(rp.report_nip())
        self.assertEqual(rp.report_nip(), error_expected)

    def testFacebook(self):
        hp = HomePage(self.driver)
        hp.click_account()
        hp.click_sign_in()
        rp = RegistrationPage(self.driver)
        rp.click_facebook_button()
        rp.accept_facebook_cookies()
        rp.enter_facebook_login(facebook_email)
        rp.enter_facebook_password(facebook_password)
        rp.click_login_facebook_button()
        rp.change_profile()
        #Check
        actual_result = rp.report_check_facebook_email()
        expected_result = facebook_email
        self.assertEqual(actual_result, expected_result)