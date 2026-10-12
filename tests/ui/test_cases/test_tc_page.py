"""Test Case page is reachable from the navbar."""

import pytest

from tests.ui.test_cases.steps import (
    delete_account_through_ui,
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc07_test_cases_page_is_opened(app):
    # Launch browser and open the site
    app.home.open()                           
    # Verify Home Page is visible                
    verify_home_page_visible(app)                             
    # Click on Signup/Login button
    app.nav.test_cases_link.click() 
    # Verify user is navigated to test cases page successfully
    assert app.test_cases.heading.is_visible()


