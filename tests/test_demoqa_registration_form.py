from demoqa_tests.data.users import User
from demoqa_tests.pages.registration_page import RegistrationPage
import datetime

Darya = User(
    first_name='Darya',
    last_name='Andronova',
    email='test@mail.ru',
    gender='Male',
    mobile_number='9111111111',
    date_of_birth=datetime.date(year=1996, month=7, day=10),
    subjects='Arts',
    hobbies='Reading',
    picture='picture.jpg',
    current_address='Testovaya Street',
    state='Uttar Pradesh',
    city='Agra'
)


def test_registration():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_registration(Darya)
    registration_page.should_have_registered(Darya)

    registration_page.close_modal()
