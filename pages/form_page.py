from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.ID, "userName")
        self.email_input = (By.ID, "userEmail")
        self.submit_button = (By.ID, "submit")
        self.confirmation_message = (By.ID, "output")

    def enter_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def click_submit(self):
        # Scroll the button into view
        button = self.driver.find_element(*self.submit_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        
        # Wait until the button is clickable
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.submit_button))
        
        # Click the button
        button.click()

    def get_confirmation_message(self):
        return self.driver.find_element(*self.confirmation_message).text
