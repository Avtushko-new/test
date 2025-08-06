import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import CalculatorPage
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_calculator_with_delay(driver):
    calculator = CalculatorPage(driver)
    
    # Открываем страницу и настраиваем задержку
    calculator.open()
    calculator.set_delay(45)
    
    # Выполняем вычисление: 7 + 8
    calculator.click_button('7')
    calculator.click_button('+')
    calculator.click_button('8')
    calculator.click_button('=')
    
    # Ждем пока исчезнет выражение и появится результат
    start_time = time.time()
    calculator.wait_for_result()
    
    result = calculator.get_result()
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    assert result == '15', f"Ожидался результат 15, получено {result}"
    assert elapsed_time >= 45, f"Вычисление заняло {elapsed_time} секунд, ожидалось не менее 45"