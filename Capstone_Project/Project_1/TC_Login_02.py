from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Orange:

    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver = webdriver.Chrome()
        self.search_username = "username"
        self.search_password = "password"
        self.submit_button = '//button[@type="submit"]'

    def browse(self):
        self.driver.get(self.url)
        print(self.driver.title)
        print("Invalid Credentials")
        self.driver.maximize_window()
        sleep(2)

    def orange_login(self):
        sleep(2)
        username_webelement = self.driver.find_element(By.NAME, self.search_username)
        username_webelement.send_keys("Admin")

        password_webelement = self.driver.find_element(By.NAME, self.search_password)
        password_webelement.send_keys("Invalid password")
        sleep(2)

        login_webelement = self.driver.find_element(By.XPATH, self.submit_button)
        login_webelement.click()
        sleep(2)


obj = Orange()
obj.browse()
obj.orange_login()
sleep(2)
