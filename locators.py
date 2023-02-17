from selenium.webdriver.common.by import By

class HomePageLocators:
    my_account_btn = (By.ID,'accountWidget')
    sign_in_btn = (By.PARTIAL_LINK_TEXT, 'zarejestruj')
    contact_side_btn = (By.XPATH, '//nav/a[9]/div/span')


class RegistrationPageLocators:
    choose_person_btn = (By.ID, 'accountType')
    choose_salut_btn = (By.ID, 'personalSalutation')
    name_input_in = (By.ID, 'personalFirstName')
    surname_input_in = (By.ID, 'personalLastName')
    email_input_in = (By.ID, 'personalMail')
    pass_input_in = (By.ID, 'personalPassword')
    address_input_in = (By.ID, 'billingAddressAddressStreet')
    post_code_input_in = (By.ID, 'billingAddressAddressZipcode')
    city_input_in = (By.ID, 'billingAddressAddressCity')
    phone_number_input_in = (By.ID, 'billingAddressAddressPhoneNumber')
    policy_input = (By.ID, "acceptedDataProtection")
    register_button_btn = (By.XPATH, '//div[5]/button')
    emailField_report = (By.NAME, "email")
    factory_input_in = (By.ID,'billingAddresscompany')
    department_input_in = (By.ID, 'billingAddressdepartment')
    NIP_input = (By.ID, "vatIds")
    # facebook
    facebook_button = (By.NAME, 'provider')
    facebook_cookies = (By.XPATH, '//button[contains(string(),"Allow essential and optional cookies")]')
    facebook_login = (By.ID, 'email')
    facebook_password = (By.ID, 'pass')
    facebook_login_button = (By.ID, 'loginbutton')
    facebook_change_profile = (By.PARTIAL_LINK_TEXT, 'Zmień')
    facebook_check = (By.CLASS_NAME, 'account-profile-mail')

class ContactFormPageLocators:
    scroll_act = (By.XPATH,'//div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div')
    choose_salut_input = (By.NAME, 'salutationId')
    name_input = (By.NAME, 'firstName')
    surname_input = (By.NAME, 'lastName')
    email_input = (By.NAME, 'email')
    phone_number_input = (By.NAME, 'phone')
    comment_input = (By.NAME, 'comment')
    subject_input = (By.NAME, 'subject')
    policy_input = (By.NAME, "privacy")
    send_button = (By.XPATH, '//form/div/button')

