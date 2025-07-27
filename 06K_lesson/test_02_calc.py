from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_slow_calculator():
    # Инициализация Chrome
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

    try:
        # 1. Открываем страницу
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

        # 2. Устанавливаем задержку 45 секунд
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # 3. Нажимаем кнопки 7 + 8 =
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # 4. Ждем результат и проверяем
        start_time = time.time()
        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )
        end_time = time.time()

        # Проверяем что прошло около 45 секунд
        elapsed_time = end_time - start_time
        print(f"Фактическое время выполнения: {elapsed_time:.2f} секунд")
        assert 45 <= elapsed_time <= 50, "Вычисления заняли неожиданное время"

        print("Тест пройден успешно! Результат 15 отобразился корректно.")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        driver.save_screenshot("error.png")
        raise

    finally:
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()
