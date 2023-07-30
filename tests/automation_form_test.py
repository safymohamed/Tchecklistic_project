import time
from pages.automation_form import Home_page

def test_automation_form(browser):
    form_object = Home_page(browser)
    first_name = "safy"
    last_name = "mohamed"
    date_input = "7/7/1987"

    form_object.load()
    # time.sleep(5)
    form_object.advertising()
    time.sleep(5)
    form_object.first_name(first_name)
    form_object.last_name(last_name)
    form_object.gender()
    form_object.experience()
    form_object.Date(date_input)
    form_object.profession()
    form_object.Tools()
    form_object.Continents()
    form_object.Selenium_Commands()
    form_object.choose_file()
    form_object.Download_file()








