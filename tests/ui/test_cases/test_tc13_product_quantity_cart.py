"""Test Case 13 Product quantity cart.

See https://automationexercise.com/test_cases
"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc13_product_quantity_cart(app):
    app.home.open()
    verify_home_page_visible(app)

    # Step 4: Click View Product for the first product
    app.home.open_product_details(app.home.featured_items.first)

    # Step 5: Verify product details page is opened
    assert app.page.url.endswith("/product_details/1")
    assert app.product_detail.info.is_visible()

    app.product_detail.set_quantity(4)
    app.product_detail.add_to_cart()
    app.product_detail.view_cart_from_modal()

    assert app.cart.rows.count() == 1
    assert app.cart.item_names.first.is_visible()
    assert app.cart.quantities.first.inner_text() == "4"