from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from elements.base_element import BaseElement
from elements.button import Button
from elements.dropdown import DropDown
from elements.input import Input
from elements.text import Text
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://accounts.google.com/"

    def __init__(self, driver: WebDriver, timeout: int):
        super().__init__(driver, timeout)
        self.greet = Text(driver, (By.CSS_SELECTOR, "span[jsslot='']"))
        self.email_input = Input(driver, (By.ID, "identifierId"))
        self.next_button = Button(driver, (By.XPATH, "//span[text()='Далее']/.."))
        self.password_input = Input(driver, (By.XPATH, "//input[@name='Passwd']"))
        self.repeat_button = Button(
            driver, (By.XPATH, "//a[@aria-label='Повторить попытку']")
        )
        self.hint_email = Text(driver, (By.CSS_SELECTOR, "div[jsname='B34EJ']"))
        self.language_switcher = DropDown(
            driver, (By.CSS_SELECTOR, "div[role='combobox']")
        )
        self.english_language = BaseElement(
            driver, (By.CSS_SELECTOR, "li[data-value='en-GB']")
        )


    def open_page(self):
        self.driver.get(self.URL)

    def enter_email(self, email):
        self.email_input.fill(email)

    def click_next(self):
        self.next_button.click()

    def enter_password(self, password):
        self.password_input.fill(password)

    def click_repeat(self):
        self.repeat_button.click()

    def switch_language_to_english(self):
        self.language_switcher.click()
        self.english_language.click()

    def is_logged_in(self):
        self.wait.until(EC.url_contains("myaccount.google.com"))
        return self.driver.current_url
