from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def get_cart_items_count(self):
        # Добавляем ожидание загрузки корзины
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
        )
        return len(self.driver.find_elements(*self.cart_items))
