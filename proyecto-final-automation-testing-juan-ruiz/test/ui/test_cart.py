import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.regression
def test_add_product_to_cart(driver):
    """
    Verifica que se pueda agregar un producto al carrito
    y que el carrito muestre al menos un ítem.
    """

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Login válido
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Validar inventory
    assert inventory_page.is_ui_loaded()
    assert inventory_page.has_products()

    # Obtener info del primer producto
    product_name = inventory_page.get_first_product_name()
    product_price = inventory_page.get_first_product_price()

    # Agregar al carrito
    inventory_page.add_first_product_to_cart()
    assert inventory_page.is_cart_badge_visible()

    # Abrir carrito
    inventory_page.open_cart()

    # Validar carrito
    assert cart_page.is_cart_page_loaded()
    assert cart_page.has_items()

    cart_name, cart_price = cart_page.get_item_name_and_price()

    assert product_name == cart_name
    assert product_price == cart_price


@pytest.mark.smoke
def test_go_to_checkout_from_cart(driver):
    """
    Verifica que desde el carrito se pueda avanzar al checkout.
    """

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Login
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Agregar producto
    inventory_page.add_first_product_to_cart()
    inventory_page.open_cart()

    # Avanzar a checkout
    cart_page.click_checkout()

    # Validar que cambió la URL
    assert "checkout-step-one" in driver.current_url
