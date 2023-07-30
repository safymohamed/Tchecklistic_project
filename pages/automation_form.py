import time
from selenium.webdriver.common.by import By

class Home_page:
    URL = 'https://www.techlistic.com/p/selenium-practice-form.html'
    first_name_element = (By.XPATH, '//input[@name="firstname"]')
    last_name_element = (By.XPATH, '//input[@name="lastname"]')
    gender_element = (By.XPATH, '//input[@value="Male"]')
    Experience_element = (By.XPATH, '//input[@value="3"]')
    Date_element = (By.ID, 'datepicker')
    profession_element = (By.XPATH, '//input[@value="Automation Tester"]')
    advertising_element = (By.XPATH, '//span[@ class="ezmob-footer-close"]')
    tools_element = (By.ID, 'tool-2')
    continent_element = (By.XPATH, '//option[text() ="North America"]')
    commands_element = (By.XPATH, '//option[text() = "WebElement Commands"]')
    choose_element = (By.ID, 'photo')
    file_element = (By.XPATH, '//a[text() ="Click here to Download File"]')


    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def advertising(self):
        advertising = self.browser.find_element(*self.advertising_element)
        advertising.click()

    def first_name(self, first_name):
        first = self.browser.find_element(*self.first_name_element)
        first.send_keys(first_name)

    def last_name(self, last_name):
        last = self.browser.find_element(*self.last_name_element)
        last.send_keys(last_name)

    def gender(self):
        gender = self.browser.find_element(*self.gender_element)
        gender.click()

    def experience(self):
        Experience  = self.browser.find_element(*self.Experience_element)
        Experience.click()

    def Date(self, date_input):
        date = self.browser.find_element(*self.Date_element)
        date.send_keys(date_input)

    def profession(self):
        profession = self.browser.find_element(*self.profession_element)
        profession.click()

    def Tools(self):
        tools = self.browser.find_element(*self.tools_element)
        tools.click()
        tools.location_once_scrolled_into_view


    def Continents(self):
        continents = self.browser.find_element(*self.continent_element)
        continents.click()

    def Selenium_Commands(self):
        command = self.browser.find_element(*self.commands_element)
        command.click()


    def choose_file(self):
        choose = self.browser.find_element(*self.choose_element)
        choose.send_keys("C:\\Users\\scs\\Desktop\\Adam Omar.png")

    def Download_file(self):
        download = self.browser.find_element(*self.file_element)
        download.click()