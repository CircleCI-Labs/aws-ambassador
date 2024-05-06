import pytest

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from app import create_app


@pytest.fixture(scope="session")
def browser():
    """
    Creates a headless chrome browser for testing
    """

    # Allows chrome to function as headless
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # Apply settings
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    yield driver

    # Quit the driver after the test
    driver.quit()


@pytest.fixture(scope="session")
def app():
    """
    Creates an instance of the Flask app
    :return: App Object
    """

    # Load the testing configuration
    config_name = "testing"
    app = create_app(config_name)

    return app


def grab_random_text_value(browser):
    """
    Grabs the random text value by ID
    :param browser: Headless browser
    :return: String
    """
    text = browser.find_element_by_id("random-text").text

    return text


def click_random_button(browser):
    """
    Clicks on the random button thus generating a random text
    :param browser: Headless browser
    :return: None
    """
    # Grab button by ID and click it
    button = browser.find_element_by_id("random-button")
    button.click()

    # Wait for the browser to be sent back to the homepage or time out
    WebDriverWait(browser, 20).until(ec.url_changes("/"), 'Timed out waiting for response')

    return None


