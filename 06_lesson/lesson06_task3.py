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
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

# 2. Дожидаемся загрузки всех картинок (ждём, пока исчезнет спиннер)
WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.ID, "spinner"))
)

# 3. Получаем все элементы с картинками
images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

# 4. Получаем значение атрибута src у 3-й картинки (индекс 2)
third_image_src = images[2].get_attribute("src")
print(third_image_src)

# Повторяем процесс
print("\nПовторяем процесс:")

# 1. Переходим на страницу
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

# 2. Дожидаемся загрузки всех картинок
WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.ID, "spinner"))
)

# 3. Получаем все элементы с картинками
images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

# 4. Получаем значение атрибута src у 3-й картинки
third_image_src = images[2].get_attribute("src")
print(third_image_src)

# Закрываем браузер
driver.quit()
