"""Test Case 16 Place order login before checkout.

See https://automationexercise.com/test_cases
"""


import pytest

from tests.ui.test_cases.steps import (
    delete_account_through_ui,
    place_order_and_pay,
    verify_home_page_visible,
    verify_logged_in_as,
    verify_address_and_review
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]

card = {
    "name": "Test User",
    "number": "4111111111111111",
    "cvc": "123",
    "expiry_month": "12",
    "expiry_year": "2030"
}


def test_tc16_place_order_login_before_checkout(app, new_user):
    # Steps 1–3: Open and verify homepage
    app.home.open()
    verify_home_page_visible(app)

    # Step 4: Click 'Signup / Login' button
    app.nav.login_link.click()

    # Steps 5-6: Fill login details and verify login
    app.login.login(new_user["email"], new_user["password"])       #6-7
    verify_logged_in_as(app, new_user["name"]) 
    
    # Steps 7–9: Add product and open cart
    product_name = app.home.featured_items.first.locator(".productinfo p").inner_text()
    app.home.add_card_to_cart(app.home.featured_items.first)
    app.home.view_cart_from_modal()

    assert app.page.url.endswith("/view_cart")    
    assert product_name in app.cart.item_names.first.inner_text()

    app.cart.proceed_to_checkout()

    # Step 11: Verify address details and order review
    verify_address_and_review(app, new_user, product_name)

    # Steps 12–15: Place order, pay, and verify confirmation
    place_order_and_pay(app, card, "Test comment")

    # Steps 16–17: Delete account and verify deletion
    delete_account_through_ui(app)
