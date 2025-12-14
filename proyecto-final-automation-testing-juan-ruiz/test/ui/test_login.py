import pytest
from pages.login_page import LoginPage
from utils.data_reader import get_valid_users, get_invalid_users


@pytest.mark.smoke
@pytest.mark.parametrize(
    "user",
    get_valid_users()
)
def test_login_success(driver, user):
    """
    Verifica que un usuario válido pueda loguearse correctamente
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(user["username"], user["password"])

    assert login_page.is_login_successful(), "El login debería ser exitoso"


@pytest.mark.regression
@pytest.mark.parametrize(
    "user",
    get_invalid_users()
)
def test_login_invalid(driver, user):
    """
    Verifica que un usuario inválido vea mensaje de error
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(user["username"], user["password"])

    error_message = login_page.get_error_message()
    assert error_message != "", "Debería mostrarse un mensaje de error"
