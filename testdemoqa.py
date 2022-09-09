from selene.support.shared import browser
from selene import command, be


def test_one():
    browser.element('#firstName').type('Elena')
    browser.element('#lastName').type('Romanova')
    browser.element('#userEmail').type('elena@mail.ru')
    browser.element('#gender-radio-2').double_click()
    browser.element('#userNumber').type('1234567891')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type("March")
    browser.element('.react-datepicker__year-select').type("1995")
    browser.element('[aria-label="Choose Monday, March 6th, 1995"]').click()
    browser.element('#subjectsInput').type('Maths').press_enter().type('History').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys()
