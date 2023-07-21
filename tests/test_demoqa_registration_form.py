from demoqa_tests.pages.registration_page import RegistrationPage


def test_registration():
    registration_page = RegistrationPage()
    registration_page.open()

    # Заполнение формы регистрации(все поля)
    registration_page.fill_first_name('Darya')
    registration_page.fill_last_name('Andronova')
    registration_page.fill_email('test@mail.ru')
    registration_page.select_gender('Male')
    registration_page.fill_mobile_number('9111111111')
    registration_page.fill_date_of_birth('1996', 'July', '10')
    registration_page.fill_subjects('Arts')
    registration_page.select_hobbies()
    registration_page.select_picture('picture.jpg')
    registration_page.fill_current_address('Testovaya Street')
    registration_page.select_state('Uttar Pradesh')
    registration_page.select_city('Agra')
    registration_page.submit()

    registration_page.should_have_registered(
        'Darya Andronova',
        'test@mail.ru',
        'Male',
        '9111111111',
        '10 July,1996',
        'Arts',
        'Reading',
        'picture.jpg',
        'Testovaya Street',
        'Uttar Pradesh Agra'
    )
    registration_page.close_modal()
