from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseElement:
    def __init__(self, driver: WebDriver, locator, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.locator = locator

    def find(self):
        return self.wait.until(EC.presence_of_element_located(self.locator))

    def click(self):
        self.find().click()

    def get_text(self):
        return self.find().text

    def is_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.locator))
