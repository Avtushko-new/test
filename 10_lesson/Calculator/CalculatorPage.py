from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class CalculatorPage:
    """Page Object для калькулятора с задержкой выполнения операций."""

    def __init__(self, driver):
        """
        Инициализирует элементы страницы.

        :param driver: WebDriver - экземпляр Selenium WebDriver
        """
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

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открывает страницу калькулятора в браузере."""
        self.driver.get("https://bonigarcia.dev/"
                        "selenium-webdriver-java/"
                        "slow-calculator.html")

    @allure.step("Установить задержку вычислений в {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку выполнения операций.

        :param seconds: int - количество секунд задержки
        """
        self.driver.find_element(*self.delay_field).clear()
        self.driver.find_element(*self.delay_field).send_keys(str(seconds))

    @allure.step("Нажать кнопку '{button}'")
    def click_button(self, button: str) -> None:
        """
        Нажимает указанную кнопку калькулятора.

        :param button: str - символ кнопки (например, '1', '+', '=')
        """
        self.driver.find_element(*self.buttons[button]).click()

    @allure.step("Ожидать результата вычислений (таймаут {timeout} сек)")
    def wait_for_result(self, timeout: int = 50) -> None:
        """
        Ожидает появления результата вычислений.

        :param timeout: int - максимальное время ожидания в секундах
        """
        WebDriverWait(self.driver, timeout).until(
            lambda d: (
                d.find_element(*self.result_field).text
                not in ['', '7+8']
            )
        )

    @allure.step("Получить результат вычислений")
    def get_result(self) -> str:
        """
        Возвращает текущий результат с экрана калькулятора.

        :return: str - текст результата
        """
        return self.driver.find_element(*self.result_field).text
