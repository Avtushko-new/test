import pytest
import sys
import os
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

# Получаем абсолютный путь к папке pages
current_dir = os.path.dirname(os.path.abspath(__file__))
pages_path = os.path.join(current_dir, 'pages')
sys.path.insert(0, pages_path)


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия драйвера."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Полный процесс оформления заказа")
@allure.description(
    "Тестирование полного цикла покупки "
    "от авторизации до подтверждения заказа"
)
def test_complete_purchase(driver):
    with allure.step("Авторизация пользователя"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        products_page = ProductsPage(driver)
        products_page.add_to_cart("Sauce Labs Backpack")
        products_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        products_page.add_to_cart("Sauce Labs Onesie")
        products_page.go_to_cart()

    with allure.step("Проверка корзины и переход к оформлению"):
        cart_page = CartPage(driver)
        with allure.step("Проверить количество товаров в корзине"):
            assert cart_page.get_cart_items_count() == 3, (
                "Ожидалось 3 товара в корзине"
            )
        cart_page.click_checkout()

    with allure.step("Заполнение данных доставки"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_shipping_info("John", "Doe", "12345")
        checkout_page.click_continue()

    with allure.step("Проверка итоговой суммы"):
        total = checkout_page.get_total_amount()
        with allure.step(
            f"Проверить что сумма равна $58.29 "
            f"(фактическая: {total})"
        ):
            assert total == "Total: $58.29", (
                f"Ожидалась сумма $58.29, получено {total}"
            )
