from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from time import sleep


def input_text_operations():
    # Настройка сервиса и опций Firefox
    service = Service(executable_path=GeckoDriverManager().install())
    options = Options()
    options.set_preference("dom.webnotifications.enabled", False)

    # Инициализация драйвера
    driver = webdriver.Firefox(service=service, options=options)

    try:
        # Открытие страницы
        driver.get("http://the-internet.herokuapp.com/inputs")
        sleep(2)

        # Находим поле ввода
        input_field = driver.find_element(
            By.CSS_SELECTOR, "input[type='number']"
        )

        # Ввод и очистка текста
        input_field.send_keys("1000")
        sleep(1)
        input_field.clear()
        sleep(1)
        input_field.send_keys("42")
        sleep(1)

        print("Все операции выполнены успешно!")

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    input_text_operations()
