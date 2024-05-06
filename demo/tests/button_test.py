import pytest

import urllib.request
from flask import url_for

from .conftest import click_random_button, grab_random_text_value


# Requires a headless browser and a instance of the Flask server
@pytest.mark.usefixtures("browser")
@pytest.mark.usefixtures("live_server")
class TestLiveServer:
    """
    Utilize an external headless browser to test the website functionality
    """

    def test_server_is_up_and_running(self):
        """
        Tests if the server is up and running
        :return:
        """
        
        # Makes a request to the page and checks status code
        res = urllib.request.urlopen(url_for("main.index", _external=True))
        assert res.code == 200

    def test_single_click(self, browser):
        """
        Clicks on the random button once and compares to result to the original value
        :param browser: A instance of a headless browser
        """
        list_of_random_text = list()

        # Grabs the initial website
        browser.get(url_for("main.index", _external=True))

        # Grabs the original value of the text, then clicks on the random button
        list_of_random_text.append(grab_random_text_value(browser))
        click_random_button(browser)

        # Grabs the random text value
        list_of_random_text.append(grab_random_text_value(browser))

        # Compares the first value in the list to the second to make sure they are not the same
        assert list_of_random_text[0] != list_of_random_text[1]

    def test_multiple_clicks(self, browser):
        """
        Clicks on the random button 3 and compares to all the results. Makes sure there are values are unique
        :param browser: A instance of a headless browser
        """
        list_of_random_text = list()

        # Grabs the initial website
        browser.get(url_for("main.index", _external=True))

        # Grabs the original value of the text, then clicks on the random button
        list_of_random_text.append(grab_random_text_value(browser))
        click_random_button(browser)

        # Grabs the random text and clicks the random button again
        list_of_random_text.append(grab_random_text_value(browser))
        click_random_button(browser)

        # Grabs the random text and clicks the random button again
        list_of_random_text.append(grab_random_text_value(browser))
        click_random_button(browser)

        # Grabs the value of the text for the final time
        list_of_random_text.append(grab_random_text_value(browser))

        # Checks is the values in the list to make sure there are no repeats
        # Checks length of the list and length of the set(sets do not allow repeats)
        assert len(list_of_random_text) == len(set(list_of_random_text))

    def test_refresh_of_page(self, browser):
        """
        Grabs the text value, refreshes the page, grabs the text value again, and then compares them
        :param browser: A instance of a headless browser
        """
        list_of_random_text = list()

        # Grabs the initial website
        browser.get(url_for("main.index", _external=True))

        # Stores the initial value of the text
        list_of_random_text.append(grab_random_text_value(browser))

        # Refreshes the page without clicking the button
        browser.refresh()

        # Grabs the text value again
        list_of_random_text.append(grab_random_text_value(browser))

        # Checks if the two values are the same
        # Thus showing that no random text was generated without clicking the button
        assert list_of_random_text[0] == list_of_random_text[1]
