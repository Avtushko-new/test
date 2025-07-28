from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService


def test_form_validation():
    # Инициализация Edge
    edge_service = EdgeService(
        executable_path=r"C:\Users\aavtu\Desktop\Инстал\msedgedriver.exe"
    )
    driver = webdriver.Edge(service=edge_service)

    try:
        # 1. Открываем страницу
        print("Открываем страницу...")
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        # 2. Заполняем форму
        print("Заполняем форму...")
        fields_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        for field_name, value in fields_data.items():
            element = driver.find_element(
                By.CSS_SELECTOR, f"input[name='{field_name}']"
            )
            element.clear()
            element.send_keys(value)

        # 3. Нажимаем Submit
        print("Отправляем форму...")
        submit_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        submit_button.click()

        # 4. Ждем появления элементов с результатами
        print("Ожидаем результатов...")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert"))
        )
        # 5. Проверяем Zip code (должен быть красным)
        print("Проверяем Zip code...")
        zip_code_element = driver.find_element(By.CSS_SELECTOR, "#zip-code")
        zip_code_classes = zip_code_element.get_attribute('class')
        print(f"Классы Zip code: {zip_code_classes}")
        assert 'alert-danger' in zip_code_classes.split(), \
            "Поле Zip code должно иметь класс alert-danger"

        # 6. Проверяем остальные поля (должны быть зелёными)
        print("Проверяем остальные поля...")
        for field_name in fields_data.keys():
            element_id = field_name.replace('-', '-')  # Оставляем как есть
            element = driver.find_element(By.CSS_SELECTOR, f"#{element_id}")
            classes = element.get_attribute('class')
            value = element.text

            print(f"Поле {field_name}: классы - {classes}, значение - {value}")

            # Проверяем класс
            assert 'alert-success' in classes.split(), (
                f"Поле {field_name} должно иметь класс alert-success"
            )

            # Проверяем значение
            assert value == fields_data[field_name], (
                f"Неверное значение {field_name}"
            )

        print("Все проверки пройдены успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        print("Текущий URL:", driver.current_url)
        driver.save_screenshot("error.png")
        raise

    finally:
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    test_form_validation()
