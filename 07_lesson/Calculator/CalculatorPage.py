from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_field = (By.CSS_SELECTOR, "#delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")
        self.buttons = {
            '1': (By.XPATH, "//span[text()='1']"),
            '2': (By.XPATH, "//span[text()='2']"),
            '3': (By.XPATH, "//span[text()='3']"),
            '4': (By.XPATH, "//span[text()='4']"),
            '5': (By.XPATH, "//span[text()='5']"),
            '6': (By.XPATH, "//span[text()='6']"),
            '7': (By.XPATH, "//span[text()='7']"),
            '8': (By.XPATH, "//span[text()='8']"),
            '9': (By.XPATH, "//span[text()='9']"),
            '0': (By.XPATH, "//span[text()='0']"),
            '+': (By.XPATH, "//span[text()='+']"),
            '-': (By.XPATH, "//span[text()='-']"),
            '*': (By.XPATH, "//span[text()='×']"),
            '/': (By.XPATH, "//span[text()='÷']"),
            '=': (By.XPATH, "//span[text()='=']"),
            'C': (By.XPATH, "//span[text()='C']")
        }

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        self.driver.find_element(*self.delay_field).clear()
        self.driver.find_element(*self.delay_field).send_keys(str(seconds))

    def click_button(self, button):
        self.driver.find_element(*self.buttons[button]).click()

    def wait_for_result(self, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*self.result_field).text not in ['', '7+8']
        )

    def get_result(self):
        return self.driver.find_element(*self.result_field).text