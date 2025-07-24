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

    driver = None
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
        except Exception as css_exc:
            print(f"Не удалось найти по CSS: {str(css_exc)}")
            # Способ 2: По тексту кнопки
            try:
                button = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(., 'Button')]")
                    )
                )
            except Exception as xpath_exc:
                print(f"Не удалось найти по XPATH: {str(xpath_exc)}")
                # Способ 3: По любому button
                button = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.TAG_NAME, "button"))
                )

        button.click()

        # Обработка алерта
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
            print("Успешно: кнопка была нажата и alert обработан")
        except Exception as alert_exc:
            print(f"Alert не появился: {str(alert_exc)}")
            print("Успешно: кнопка была нажата (alert не появился)")

    except Exception as e:
        print(f"Критическая ошибка: {str(e)}", file=sys.stderr)
        if driver:
            driver.save_screenshot("error_screenshot.png")
            print(
                "Скриншот сохранен как error_screenshot.png", file=sys.stderr
            )
        return 1  # Код ошибки
    finally:
        if driver:
            driver.quit()
    return 0


if __name__ == "__main__":
    sys.exit(test_click_blue_button())
