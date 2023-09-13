from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

# from webdriver_manager.core import driver


class Orange:

    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver = webdriver.Chrome()
        self.search_username = "username"
        self.search_password = "password"
        self.submit_button = '//button[@type="submit"]'
        self.admin = '//a[@href="/web/index.php/admin/viewAdminModule"]'
        self.options_to_validate = [
            "Admin",
            "PIM",
            "Leave",
            "Time",
            "Recruitment",
            "My Info",
            "Performance",
            "Dashboard",
            "Directory",
            "Maintenance",
            "Buzz"
        ]

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

        for option in self.options_to_validate:
            try:
                option_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, option)
                print(option_element)
                print(f"Option '{option}' is available.")
            except NoSuchElementException:
                print(f"Option '{option}' is not available.")


obj = Orange()
obj.browse()
obj.orange_login()
sleep(2)
