from Pages.home_page import HomePage
from Pages.contact_page import ContactForm
from Tests.test_base import BaseTest
from data import sex, name, surname, email_correct, phone_number, comment, fakename, fakesurname


class ContactTest(BaseTest):
    def testContactForm(self):
        hp = HomePage(self.driver)
        hp.click_contact()
        cf= ContactForm(self.driver)
        cf.scroll_action()
        cf.choose_salut(sex)
        cf.enter_name(fakename)
        cf.enter_surname(fakesurname)
        cf.enter_email(email_correct)
        cf.enter_phonenumber(phone_number)
        cf.enter_comment(comment)
        cf.policy_click()
        cf.send_click()
        cf.report_no_title()
        error_expected = "Please fill out this field."
        print(cf.report_no_title())
        self.assertEqual(cf.report_no_title(), error_expected)