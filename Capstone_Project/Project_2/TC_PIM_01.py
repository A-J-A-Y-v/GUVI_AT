from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Orange:

    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver = webdriver.Chrome()
        self.forgot_password = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p'
        self.username = "username"
        self.submit_button = '//button[@type="submit"]'

    def browse(self):
        self.driver.get(self.url)
        print("Reset password link sent successfully")
        self.driver.maximize_window()
        sleep(2)

    def orange_login(self):
        sleep(2)
        forgot_password_webelement = self.driver.find_element(By.XPATH, self.forgot_password)
        forgot_password_webelement.click()
        sleep(2)

        username_webelement = self.driver.find_element(By.NAME, self.username)
        username_webelement.send_keys("Admin")
        sleep(2)

        submit_webelement = self.driver.find_element(By.XPATH, self.submit_button)
        submit_webelement.click()
        sleep(2)


obj = Orange()
obj.browse()
obj.orange_login()
sleep(2)
