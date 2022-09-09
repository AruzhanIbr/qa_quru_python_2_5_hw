import os
from selene import have
from selene.support.shared import browser


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
    browser.element('#uploadPicture').send_keys(os.path.abspath('files/test.jpg'))
    browser.element('#currentAddress').type('Astana')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.modal-body td+td').should(have.texts(
        'Elena Romanova',
        'elena@mail.ru',
        'Female',
        '1234567891',
        '06 March,1995',
        'Maths, History',
        'Reading',
        'test.jpg',
        'Astana',
        'Haryana Karnal'))






