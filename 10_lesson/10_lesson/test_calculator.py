import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import CalculatorPage


@allure.feature("Тесты калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    @pytest.fixture
    def driver(self):
        """Фикстура для инициализации и закрытия драйвера."""
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
            )
        yield driver
        driver.quit()

    @allure.title("Проверка вычислений с задержкой")
    @allure.description(
        "Тестирование работы калькулятора с установленной задержкой "
        "выполнения операций"
    )
    def test_calculator_with_delay(self, driver):
        calculator = CalculatorPage(driver)

        with allure.step("Открыть и настроить калькулятор"):
            calculator.open()
            calculator.set_delay(45)

        with allure.step("Выполнить вычисление 7 + 8"):
            calculator.click_button('7')
            calculator.click_button('+')
            calculator.click_button('8')
            calculator.click_button('=')

        with allure.step("Измерить время выполнения"):
            start_time = time.time()
            calculator.wait_for_result()
            result = calculator.get_result()
            end_time = time.time()
            elapsed_time = end_time - start_time

        with allure.step("Проверить результат и время выполнения"):
            assert result == '15', f"Ожидался результат 15, получено {result}"
            assert elapsed_time >= 45, (
                f"Вычисление заняло {elapsed_time} секунд, "
                f"ожидалось не менее 45"
            )
