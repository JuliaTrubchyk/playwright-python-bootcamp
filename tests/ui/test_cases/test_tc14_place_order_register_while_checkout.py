"""Test Case 14 Place order register while checkout.

See https://automationexercise.com/test_cases
"""


import pytest

from tests.ui.test_cases.steps import (
    delete_account_through_ui,
    place_order_and_pay,
    sign_up_through_ui,
    verify_address_and_review,
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]

card = {
    "name": "Test User",
    "number": "4111111111111111",
    "cvc": "123",
    "expiry_month": "12",
    "expiry_year": "2030"
}


def test_tc14_place_order_register_while_checkout(app, signup_user):
    app.home.open()
    verify_home_page_visible(app)

    # Steps 4–6: Add product and open cart
    product_name = app.home.featured_items.first.locator(".productinfo p").inner_text()
    app.home.add_card_to_cart(app.home.featured_items.first)
    app.home.view_cart_from_modal()
    assert app.page.url.endswith("/view_cart")

    # Steps 7–8: Proceed to checkout and register
    app.cart.proceed_to_checkout()
    app.cart.register_login_link.click()

    # Steps 9–11: Create account and verify login
    sign_up_through_ui(app, signup_user)
    verify_logged_in_as(app, signup_user["name"]) 

    # Steps 12–13: Return to checkout
    app.nav.cart_link.click()
    app.cart.proceed_to_checkout()

    # Step 14: Verify address details and order review
    verify_address_and_review(app, signup_user, product_name)

    # Steps 15–18: Place order, pay, and verify confirmation
    place_order_and_pay(app, card, "Test comment")

    # Steps 19–20: Delete account and verify deletion
    delete_account_through_ui(app)
