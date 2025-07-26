from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


def login_and_get_message():
    # Указание пути к geckodriver
    service = Service(executable_path=GeckoDriverManager().install())

    # Настройка сервиса Firefox
    options = webdriver.FirefoxOptions()

    # Инициализация драйвера
    driver = webdriver.Firefox(service=service, options=options)

    try:
        # Открытие страницы авторизации
        driver.get("http://the-internet.herokuapp.com/login")
        sleep(2)

        # Ввод логина
        username = driver.find_element(By.ID, "username")
        username.send_keys("tomsmith")
        sleep(1)

        # Ввод пароля
        password = driver.find_element(By.ID, "password")
        password.send_keys("SuperSecretPassword!")
        sleep(1)

        # Нажатие кнопки Login
        login_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        login_button.click()
        sleep(2)  # Ожидание загрузки после авторизации

        # Получение текста из зеленой плашки
        flash_message = driver.find_element(By.ID, "flash")
        # Убираем кнопку закрытия из текста
        message_text = flash_message.text.split("\n")[0]
        print("Сообщение после авторизации:", message_text)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    login_and_get_message()
