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

# 1. Открываем страницу
driver.get("http://uitestingplayground.com/ajax")

# 2. Находим и нажимаем кнопку
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# 3. Ожидаем и выводим текст
green_banner = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)
print(green_banner.text)

# Закрываем браузер
driver.quit()
