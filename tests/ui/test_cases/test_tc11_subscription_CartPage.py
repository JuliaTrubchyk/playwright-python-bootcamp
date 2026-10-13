"""Test Case 11 Subscription CartPage.

See https://automationexercise.com/test_cases
"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc11_subscription_CartPage(app):
    app.home.open()
    verify_home_page_visible(app)

    app.nav.cart_link.click()

    assert app.footer.heading.is_visible()
    app.footer.subscribe("test@example.com")

    assert app.footer.success_message.is_visible()