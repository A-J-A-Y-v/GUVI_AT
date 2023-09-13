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
        self.pim_button = '//a[@href="/web/index.php/pim/viewPimModule"]'
        self.delete_button = '//input[@value="33"]'
        self.confirm_delete = '//button[@type="button"]'

    def browse(self):
        self.driver.get(self.url)
        print(self.driver.title)
        self.driver.maximize_window()
        sleep(2)

    def orange_login(self):
        sleep(2)
        username_webelement = self.driver.find_element(By.NAME, self.search_username)
        username_webelement.send_keys("Admin")

        password_webelement = self.driver.find_element(By.NAME, self.search_password)
        password_webelement.send_keys("admin123")
        sleep(2)

        login_webelement = self.driver.find_element(By.XPATH, self.submit_button)
        login_webelement.click()
        sleep(2)

    def user_delete(self):
        sleep(2)
        pim_webelement = self.driver.find_element(By.XPATH, self.pim_button)
        pim_webelement.click()
        sleep(1)

        delete_webelement_element = self.driver.find_element(By.XPATH, self.delete_button)
        delete_webelement_element.click()
        sleep(1)

        confirm_delete_element = self.driver.find_element(By.XPATH, self.confirm_delete)
        confirm_delete_element.click()
        sleep(1)


obj = Orange()
obj.browse()
obj.orange_login()
sleep(2)
obj.user_delete()
sleep(2)
