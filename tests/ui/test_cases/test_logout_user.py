"""Test Case 4: Valid user can logout.

See https://automationexercise.com/test_cases
"""

import pytest

from tests.ui.test_cases.steps import (
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]

def test_tc04_logout_user(app, new_user):

    app.home.open()
    verify_home_page_visible(app)
    app.nav.login_link.click()

    assert app.login.login_heading.inner_text() == "Login to your account"

    app.login.login(new_user["email"], new_user["password"])
    verify_logged_in_as(app, new_user["name"])

    app.nav.logout_link.click()

    assert app.page.url.endswith("/login")
    assert app.login.login_heading.is_visible()
