import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.regression
def test_checkout_process(driver):
    """
    Verifica el proceso completo de checkout:
    - Agregar un producto al carrito
    - Ir al carrito
    - Completar formulario de checkout
    - Validar compra completada
    """

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Login válido
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_login_successful()

    # Agregar producto al carrito
    inventory_page.add_first_product_to_cart()
    assert inventory_page.is_cart_badge_visible()

    # Ir al carrito y verificar ítem
    inventory_page.open_cart()
    assert cart_page.has_items()

    # Proceso de checkout
    cart_page.click_checkout()
    checkout_page.fill_checkout_form("Juan", "Ruiz", "12345")
    checkout_page.click_continue()

    # Finalizar compra
    checkout_page.click_finish()

    # Verificar que la compra fue exitosa
    assert checkout_page.is_order_completed()
