"""Test Case 10 Subscription HomePage.

See https://automationexercise.com/test_cases
"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc10_subscription_HomePage(app):
    app.home.open()
    verify_home_page_visible(app)

    assert app.footer.heading.is_visible()
    app.footer.subscribe("test@example.com")

    assert app.footer.success_message.is_visible()
