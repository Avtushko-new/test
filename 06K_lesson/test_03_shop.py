from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time


def test_sauce_demo_purchase():
    # Инициализация Firefox
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )

    try:
        # 1. Открываем сайт
        driver.get("https://www.saucedemo.com/")

        # 2. Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 3. Добавляем товары в корзину
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for item_name in items_to_add:
            item_xpath = (
                f"//div[text()='{item_name}']/"
                "ancestor::div[@class='inventory_item_description']//button"
            )
            driver.find_element(By.XPATH, item_xpath).click()
            print(f"Добавлен товар: {item_name}")
            time.sleep(1)  # Небольшая пауза между добавлениями

        # 4. Переходим в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # 5. Начинаем оформление заказа
        driver.find_element(By.ID, "checkout").click()

        # 6. Заполняем форму
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        # 7. Получаем итоговую стоимость
        total_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
                )
        )
        total_text = total_element.text
        total_value = total_text.replace("Total: $", "")

        print(f"Итоговая стоимость: {total_text}")

        # 8. Проверяем сумму
        assert total_value == "58.29", (
            f"Ожидалась сумма $58.29, получено ${total_value}"
        )

        print("Тест пройден успешно! Итоговая сумма корректна.")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        driver.save_screenshot("error.png")
        raise

    finally:
        driver.quit()


if __name__ == "__main__":
    test_sauce_demo_purchase()
