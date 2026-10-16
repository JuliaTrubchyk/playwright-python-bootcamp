"""Test Case 20 Search product and verify cart after login.

See https://automationexercise.com/test_cases
"""

import pytest

from tests.ui.test_cases.steps import (
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc20_search_product_verify_cart_after_login(app, new_user):
    app.home.open()
    verify_home_page_visible(app)

    app.nav.products_link.click()
    assert app.products.heading.is_visible()

    app.products.search("jeans")
    assert app.products.searched_heading.is_visible()

    # Verify all products related to search are visible
    names = app.products.names.all()

    assert len(names) > 0

    for name in names:
        assert name.is_visible()

    # Add products to cart
    card_count = app.products.cards.count()

    for i in range(card_count - 1):
        app.products.add_to_cart(i)

    # Add the last product separately and view cart
    app.products.add_card_to_cart(app.products.cards.nth(card_count - 1))
    app.products.view_cart_from_modal()
    assert app.page.url.endswith("/view_cart")
    assert app.cart.rows.count() == card_count

    # Login as a valid user
    app.nav.login_link.click()
    app.login.login(new_user["email"], new_user["password"])       #6-7
    verify_logged_in_as(app, new_user["name"]) 

    # Navigate to cart page and verify contents
    app.nav.cart_link.click()
    assert app.page.url.endswith("/view_cart")
    assert app.cart.rows.count() == card_count