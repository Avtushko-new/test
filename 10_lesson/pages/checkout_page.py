from selenium.webdriver.common.by import By
import allure


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    def __init__(self, driver):
        """
        Инициализирует элементы страницы оформления.

        :param driver: WebDriver - экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_amount = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить информацию о доставке")
    def fill_shipping_info(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> None:
        """
        Заполняет форму доставки.

        :param first_name: str - имя
        :param last_name: str - фамилия
        :param postal_code: str - почтовый индекс
        """
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(
            *self.postal_code_field
        ).send_keys(postal_code)

    @allure.step("Нажать кнопку продолжения")
    def click_continue(self) -> None:
        """Кликает по кнопке продолжения оформления заказа."""
        self.driver.find_element(*self.continue_button).click()

    @allure.step("Получить итоговую сумму")
    def get_total_amount(self) -> str:
        """
        Возвращает итоговую сумму заказа.

        :return: str - текст с итоговой суммой
        """
        return self.driver.find_element(*self.total_amount).text
