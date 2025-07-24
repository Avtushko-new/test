from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from time import sleep


def input_text_operations():
    # Указание явного пути к geckodriver
    gecko_path = r"C:\Users\aavtu\Desktop\Инстал\geckodriver.exe"

    # Инициализация сервиса Firefox
    service = Service(executable_path=gecko_path)

    # Настройка опций Firefox
    options = webdriver.FirefoxOptions()
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
        input_field.send_keys("Sky")
        sleep(1)
        input_field.clear()
        sleep(1)
        input_field.send_keys("Pro")
        sleep(1)

        print("Все операции выполнены успешно!")

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    input_text_operations()
