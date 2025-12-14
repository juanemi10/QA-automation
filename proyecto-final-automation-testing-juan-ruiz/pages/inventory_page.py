from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

logger = get_logger()


class InventoryPage:

    # Locators
    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    FIRST_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    FIRST_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title(self):
        logger.info("Obteniendo título de la página")
        return self.wait.until(EC.visibility_of_element_located(self.TITLE)).text

    def has_products(self):
        logger.info("Verificando presencia de productos")
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return len(items) > 0

    def get_first_product_name(self):
        logger.info("Obteniendo nombre del primer producto")
        return self.wait.until(
            EC.visibility_of_element_located(self.FIRST_ITEM_NAME)
        ).text

    def get_first_product_price(self):
        logger.info("Obteniendo precio del primer producto")
        return self.wait.until(
            EC.visibility_of_element_located(self.FIRST_ITEM_PRICE)
        ).text

    def add_first_product_to_cart(self):
        logger.info("Agregando primer producto al carrito")
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        ).click()

    def is_cart_badge_visible(self):
        logger.info("Verificando contador del carrito")
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        ).is_displayed()

    def open_cart(self):
        logger.info("Abriendo carrito")
        self.driver.find_element(*self.CART_LINK).click()

    def is_ui_loaded(self):
        logger.info("Verificando elementos clave de UI")
        self.wait.until(EC.visibility_of_element_located(self.MENU_BUTTON))
        self.wait.until(EC.visibility_of_element_located(self.FILTER_DROPDOWN))
        return True
