"""Test Case 17 Remove from cart.

See https://automationexercise.com/test_cases
"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc17_remove_product_from_cart(app):
    app.home.open()
    verify_home_page_visible(app)

    # Add first product
    app.home.add_card_to_cart(app.home.featured_items.nth(0))
    app.home.continue_shopping()

    # Add second product
    app.home.add_card_to_cart(app.home.featured_items.nth(1))
    app.home.view_cart_from_modal()

    assert app.page.url.endswith("/view_cart")
    assert app.cart.rows.count() == 2

    app.cart.remove_first_item()
    assert app.cart.rows.count() == 1