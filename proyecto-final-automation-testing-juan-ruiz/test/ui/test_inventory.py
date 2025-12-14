import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.regression
def test_inventory_page(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")
    assert login.is_login_successful()

    # Validar título
    title = inventory.get_title()
    assert title == "Products"

    # Validar presencia de productos
    assert inventory.has_products()

    # Obtener nombre y precio del primer producto
    name = inventory.get_first_product_name()
    price = inventory.get_first_product_price()
    print(f"Primer producto: {name} - {price}")

    # Validar UI
    assert inventory.is_ui_loaded()
