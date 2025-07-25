from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import warnings


def click_dynamic_button():
    # Фильтрация предупреждений
    warnings.filterwarnings("ignore")

    # Настройка Chrome с опциями
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Инициализация драйвера
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    sleep(2)

    try:
        # Открытие страницы
        driver.get("http://uitestingplayground.com/dynamicid")
        sleep(2)

        # Поиск и клик по кнопке
        button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
        button.click()
        sleep(2)

        print("Успех: синяя кнопка была нажата")

    except Exception as e:
        print(f"Ошибка: {str(e)}")
    finally:
        driver.quit()


if __name__ == "__main__":
    click_dynamic_button()
