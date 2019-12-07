from bs4 import BeautifulSoup
from selenium import webdriver
import time


def login(username, password, driver):
    driver.get("https://wsp.kbtu.kz/AttestationView")
    # Give the javascript time to render
    driver.implicitly_wait(5)
    time.sleep(6)

    #fill username
    username_field = driver.find_element_by_xpath("//input[@type='text']")
    username_field.send_keys(username)

    #fill password
    password_field = driver.find_element_by_xpath("//input[@type='password']")
    password_field.send_keys(password)

    #submit
    submit_button = driver.find_element_by_class_name("v-button-primary")
    submit_button.click()


if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    driver.set_window_size(1024, 768)
    login("z_aman", "password", driver)

#driver.quit()