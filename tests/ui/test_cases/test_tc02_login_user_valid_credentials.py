"""Test Case 2 Login user with correct email and password.

See https://automationexercise.com/test_cases
"""

import pytest

from tests.ui.test_cases.steps import (
    delete_account_through_ui,
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]

# Positive Login Test Case
def test_tc02_login_valid(app, new_user):
    app.home.open()
    verify_home_page_visible(app)
    app.nav.login_link.click()

    assert app.login.login_heading.inner_text() == "Login to your account"  #5

    app.login.login(new_user["email"], new_user["password"])       #6-7
    verify_logged_in_as(app, new_user["name"])                     #8

    delete_account_through_ui(app)                            #9-10
