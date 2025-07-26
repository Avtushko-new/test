from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# 1. Переходим на страницу
driver.get("http://uitestingplayground.com/textinput")

# 2. Находим поле ввода и вводим текст "SkyPro"
input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.clear()
input_field.send_keys("SkyPro")

# 3. Находим и нажимаем синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
blue_button.click()

# 4. Получаем обновлённый текст кнопки
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#updatingButton"), "SkyPro"
    )
)
button_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(button_text)  # Выведет "SkyPro"

# Закрываем браузер
driver.quit()
