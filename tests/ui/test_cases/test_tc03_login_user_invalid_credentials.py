"""Test Cases 3.1 and 3.2: Login flows.

- TC03.1: Login user with incorrect email and correct password.
- TC03.2: Login user with valid email and incorrect password.
See https://automationexercise.com/test_cases
"""

import pytest

from tests.ui.test_cases.steps import (
    verify_home_page_visible
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


# Negative Login Test Case
def test_tc03_login_invalid_email(app, new_user):
    app.home.open()
    verify_home_page_visible(app)
    app.nav.login_link.click()

    assert app.login.login_heading.inner_text() == "Login to your account"  #5

    app.login.login("nonexistent.user@example.com", new_user["password"])      

    assert app.login.error_message.is_visible()

def test_tc03_login_invalid_password(app, new_user):
    app.home.open()
    verify_home_page_visible(app)
    app.nav.login_link.click()

    assert app.login.login_heading.inner_text() == "Login to your account"  #5

    app.login.login(new_user["email"], "wrong_password")      

    assert app.login.error_message.is_visible()
                  