import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.form_page import FormPage

def test_demoqa_form_submission():
    # Setup WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/text-box")

    # Create page object
    form = FormPage(driver)

    # Test data
    name = "Poison Test"
    email = "poison@test.com"

    # Steps
    form.enter_name(name)
    form.enter_email(email)
    form.click_submit()

    # Assertion
    confirmation = form.get_confirmation_message()
    assert name in confirmation and email in confirmation

    # Close browser
    driver.quit()
