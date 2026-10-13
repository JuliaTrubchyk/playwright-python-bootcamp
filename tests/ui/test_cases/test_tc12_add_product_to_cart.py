"""Test Case 12 Add product to cart.

See https://automationexercise.com/test_cases
"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc12_add_product_to_cart(app):
    app.home.open()
    verify_home_page_visible(app)

    app.nav.products_link.click() 
    assert app.products.heading.is_visible()

    app.products.add_to_cart(0)
    app.products.add_card_to_cart(app.products.cards.nth(1))
    app.products.view_cart_from_modal()
    assert app.page.url.endswith("/view_cart")

    # Verify both products' prices, quantities and total prices
    assert app.cart.rows.count() == 2

    for i in range(2):
        price = app.cart.unit_prices.nth(i).inner_text()
        quantity = app.cart.quantities.nth(i).inner_text()
        total = app.cart.totals.nth(i).inner_text()

        assert price
        assert quantity == "1"

        # Convert price strings like "Rs. 500" to integers
        price_value = int(price.replace("Rs.", "").strip())
        total_value = int(total.replace("Rs.", "").strip())

        assert total_value == price_value * int(quantity)
