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
        self.edit_button = '//*[@id="app"]/div[1]/div[2]/div[2]//div[2]/div[3]//div[2]/div[8]/div/div[9]//button[2]/i'
        self.lastname = "lastname"
        self.middlename = "middlename"

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
        sleep(1)

    def user_edit(self):
        sleep(1)
        pim_webelement = self.driver.find_element(By.XPATH, self.pim_button)
        pim_webelement.click()
        sleep(3)

        edit_button_webelement = self.driver.find_element(By.XPATH, self.edit_button)
        edit_button_webelement.click()
        sleep(3)

        lastname_webelement = self.driver.find_element(By.XPATH, self.lastname)
        lastname_webelement.send_keys("Admin")

        middlename_webelement = self.driver.find_element(By.XPATH, self.middlename)
        middlename_webelement.send_keys("admin123")
        sleep(2)


obj = Orange()
obj.browse()
obj.orange_login()
sleep(2)
obj.user_edit()
sleep(2)
