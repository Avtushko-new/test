from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    """Page Object для страницы корзины интернет-магазина."""

    def __init__(self, driver):
        """
        Инициализирует элементы страницы корзины.

        :param driver: WebDriver - экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    @allure.step("Нажать кнопку оформления заказа")
    def click_checkout(self) -> None:
        """Кликает по кнопке оформления заказа."""
        self.driver.find_element(*self.checkout_button).click()

    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self) -> int:
        """
        Возвращает количество товаров в корзине.

        :return: int - количество элементов в корзине
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
        )
        return len(self.driver.find_elements(*self.cart_items))
