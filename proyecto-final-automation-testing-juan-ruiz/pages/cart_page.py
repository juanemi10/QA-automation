from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

logger = get_logger()


class CartPage:

    CART_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.cart_button")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_cart_page_loaded(self):
        logger.info("Verificando que el carrito esté cargado")
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_TITLE)
        ).is_displayed()

    def has_items(self):
        logger.info("Verificando productos en el carrito")
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items) > 0

    def get_item_name_and_price(self):
        logger.info("Obteniendo nombre y precio del producto")
        name = self.wait.until(
            EC.visibility_of_element_located(self.ITEM_NAME)
        ).text
        price = self.driver.find_element(*self.ITEM_PRICE).text
        return name, price

    def remove_first_item(self):
        logger.info("Eliminando primer producto del carrito")
        self.wait.until(
            EC.element_to_be_clickable(self.REMOVE_BUTTON)
        ).click()

    def click_checkout(self):
        logger.info("Click en botón Checkout")
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
