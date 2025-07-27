from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import sys


def test_click_blue_button():
    """Test clicking the blue button with comprehensive error handling."""
    # Настройка Chrome с игнорированием SSL ошибок
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    try:
        # Инициализация драйвера
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        driver.get("http://uitestingplayground.com/classattr")

        # Попробуем несколько способов найти кнопку
        try:
            # Способ 1: Ожидание по CSS классу
            button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "button.btn-primary")
                )
            )
            button.click()
        except Exception as css_exc:
            print(f"Не удалось найти по CSS: {str(css_exc)}")

    finally:
        driver.quit()


if __name__ == "__main__":
    sys.exit(test_click_blue_button())
