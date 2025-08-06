import pytest
import sys
import os
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
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_complete_purchase(driver):
    # Авторизация
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Добавление товаров
    products_page = ProductsPage(driver)
    products_page.add_to_cart("Sauce Labs Backpack")
    products_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    products_page.add_to_cart("Sauce Labs Onesie")
    products_page.go_to_cart()

    # Переход к оформлению заказа
    cart_page = CartPage(driver)
    assert cart_page.get_cart_items_count() == 3
    cart_page.click_checkout()

    # Заполнение данных
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_shipping_info("John", "Doe", "kfufns!~ldfj")
    checkout_page.click_continue()

    # Проверка итоговой суммы
    total = checkout_page.get_total_amount()
    assert total == "Total: $58.29", (
        f"Ожидалась сумма $58.29, получено {total}"
    )
