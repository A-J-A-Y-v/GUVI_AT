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
        self.drop_down_button = '//span[@class="oxd-userdropdown-tab"]//p'
        self.pim_button = '//a[@href="/web/index.php/pim/viewPimModule"]'
        self.add_employee = '//a[text()="Add Employee"]'
        self.firstname = "firstname"
        self.lastname = "lastname"
        self.save_button = '//button[@type="submit"]'
        self.license_date = "yyyy-mm-dd"
        self.gender = '//span[@class="oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input"]//p'

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

    def user_creation(self):
        sleep(2)
        pim_webelement = self.driver.find_element(By.XPATH, self.pim_button)
        pim_webelement.click()
        sleep(2)

        add_employee_element = self.driver.find_element(By.XPATH, self.add_employee)
        add_employee_element.click()
        sleep(2)

        firstname_webelement = self.driver.find_element(By.NAME, self.firstname)
        firstname_webelement.send_keys("guvi")
        sleep(2)

        lastname_webelement = self.driver.find_element(By.XPATH, self.lastname)
        lastname_webelement.send_keys("demo")
        sleep(2)

        save_webelement = self.driver.find_element(By.XPATH, self.save_button)
        save_webelement.click()
        sleep(2)

        license_webelement = self.driver.find_element(By.NAME, self.license_date)
        license_webelement.send_keys("2023-04-04")
        sleep(2)

        save_webelement = self.driver.find_element(By.XPATH, self.save_button)
        save_webelement.click()
        sleep(2)


obj = Orange()
obj.browse()
obj.orange_login()
sleep(2)
obj.user_creation()
sleep(2)
