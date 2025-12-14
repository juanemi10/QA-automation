import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.screenshot import take_screenshot
from utils.logger import get_logger

logger = get_logger()


@pytest.fixture
def driver(request):
    """
    Fixture que inicializa y cierra el navegador por cada test
    """
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    logger.info("Browser iniciado")

    yield driver

    if request.node.rep_call.failed:
        logger.error(f"Test fallido: {request.node.name}")
        take_screenshot(driver, request.node.name)

    driver.quit()
    logger.info("Browser cerrado")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook para detectar si el test falló
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
