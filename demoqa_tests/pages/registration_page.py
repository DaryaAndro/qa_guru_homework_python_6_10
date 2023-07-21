from selene import browser, have

from tests.conftest import path


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month').click()

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def select_gender(self, value):
        browser.all('#genterWrapper .custom-control').element_by(have.exact_text(value)).click()

    def fill_mobile_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def select_hobbies(self):
        browser.element('[for=hobbies-checkbox-2]').click()

    def select_picture(self, filename):
        browser.element('#uploadPicture').send_keys(path(filename))

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def select_state(self, value):
        browser.element('#state').click()
        browser.all('#state div').element_by(have.exact_text(value)).click()

    def select_city(self, value):
        browser.element('#city').click()
        browser.all('#city div').element_by(have.exact_text(value)).click()

    def submit(self):
        browser.element('#submit').press_enter()

    def should_have_registered(self, full_name, email, gender, mobile_number, date_of_birth,
                               subjects, hobbies, picture, current_address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile_number,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                current_address,
                state_and_city
            )
        )

    def close_modal(self):
        browser.element('#closeLargeModal').should(have.exact_text('Close')).click()
