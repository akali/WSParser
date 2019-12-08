from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Parser:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.set_window_size(1024, 768)

    def login(self):
        self.driver.get("https://wsp.kbtu.kz/AttestationView")
        # Give the javascript time to render
        self.driver.implicitly_wait(5)
        time.sleep(6)

        # fill password
        password_field = self.driver.find_element_by_xpath("//input[@type='password']")
        password_field.send_keys(self.password)

        # fill username
        username_field = self.driver.find_element_by_xpath("//input[@type='text']")
        username_field.send_keys(self.username)

        # submit
        submit_button = self.driver.find_element_by_class_name("v-button-primary")
        submit_button.click()

    def get_schedule(self, year, semester):
        self.driver.get("https://wsp.kbtu.kz/StudentSchedule")
        # Give the javascript time to render
        self.driver.implicitly_wait(5)
        time.sleep(6)

        year_field = self.driver.find_elements_by_xpath("//input[@class='v-filterselect-input']")[0]
        # year_field.clear() doesnt for
        for i in range(9):
            year_field.send_keys(Keys.BACK_SPACE)

        # trim last character to fill with help of autofill
        year_field.send_keys(year[:-1])
        year_field.send_keys(Keys.RETURN)
        year_field.send_keys(Keys.RETURN)
        time.sleep(2)

        semester_field = self.driver.find_elements_by_xpath("//input[@class='v-filterselect-input']")[1]
        # year_field.clear() doesnt for
        for i in range(9):
            semester_field.send_keys(Keys.BACK_SPACE)

        # trim last character to fill with help of autofill
        semester_field.send_keys(semester[:-1])
        semester_field.send_keys(Keys.RETURN)


if __name__ == '__main__':
    test = Parser("z_aman", "Password")
    test.login()
    time.sleep(6)
    test.get_schedule("2018-2010", "Весенний")

# driver.quit()
