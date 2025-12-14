import pytest
from pages.login_page import LoginPage
from utils.helpers import load_users


@pytest.mark.regression
@pytest.mark.parametrize("user", load_users("invalid"))
def test_login_invalid(driver, user):
    login = LoginPage(driver)

    login.open()
    login.login(user["username"], user["password"])

    error_message = login.get_error_message()
    assert "Epic sadface" in error_message
