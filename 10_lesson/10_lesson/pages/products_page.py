from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, product_name):
        items = self.driver.find_elements(*self.inventory_items)
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == product_name:
                # Добавляем ожидание перед кликом
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "button.btn_inventory")
                    )
                )
                item.find_element(
                    By.CSS_SELECTOR, "button.btn_inventory"
                ).click()
                break

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
