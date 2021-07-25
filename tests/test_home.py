import pytest
from testlib.pages.homepage import HomePage
HP = HomePage()

class TestHome:
    def test_home_logo_displayed(self):
        # print("teeest")
        logo = HP.check_page_loaded().is_displayed()
        assert logo == True

    def test_user_button(self):
        user_button = HP.check_user_button()
        assert user_button.is_displayed() == True

        user_button.click()

    