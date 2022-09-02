from faker import Faker


fake = Faker()
type_account = 'private'
type_account2 = 'business'
factory = 'Testowa firma XXX'
department = 'IT'
email = "@wp.pl"
email_correct = "test@wp.pl"
sex = 'male'
name = 'Iza'
surname = 'Test'
password = 'adminxyz'
password_short = "test"
address = 'Wrocław ul. Sztasica 5'
street_l = address.split(' ')
street = street_l[1] + ' ' + street_l[2] + ' ' + street_l[3]
city = address[0]
birthday = "1996-10-21"
post_code = '90-999'
phone_number = '111222333'
alias = 'test'
fakename = fake.first_name()
fakesurname = fake.last_name()
fakebirthday = fake.date_of_birth()
comment = fake.text()
