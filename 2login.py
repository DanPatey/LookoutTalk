from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from data.user import user


class Login(object):

    def __init__(self, driver):
        self.driver = driver

    def load_page(self, env):
        self.driver.get('https://' + env + '.mywebsite.com/')

    def login(self, email, password):
        self.driver.find_element(By.ID, 'id_username').send_keys(email + Keys.TAB)
        self.driver.find_element(By.ID, 'id_password').send_keys(password)
        self.driver.find_element(By.ID, 'id_submit_button').click()

    def login_as_user(self, user):
        self.driver.find_element(By.ID, 'id_username').send_keys(user['email'] + Keys.TAB)
        self.driver.find_element(By.ID, 'id_password').send_keys(user['password'])
        self.driver.find_element(By.ID, 'id_submit_button').click()

    def as_user(self, user):
        try:
            loginWidget = self.driver.find_element(By.ID, 'id_login_widget_user').getText()
            response = self.assertEqual(loginWidget, user['widget'])
        except Exception as e:
            self.login_as_user(user)

    def as_mywebsite_user(self, identifier):
        return self.as_user(users.users[identifier])
