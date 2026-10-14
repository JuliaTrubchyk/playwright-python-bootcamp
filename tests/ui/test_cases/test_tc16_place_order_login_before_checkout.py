"""Test Case 16 Place order login before checkout.

See https://automationexercise.com/test_cases
"""


import pytest

from tests.ui.test_cases.steps import (
    delete_account_through_ui,
    place_order_and_pay,
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


def test_tc16_place_order_login_before_checkout(app, new_user):
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

    app.cart.proceed_to_checkout()

    # Step 11: Verify Address Details
    delivery = app.checkout.delivery_address
    billing = app.checkout.billing_address

    assert delivery.is_visible()
    assert billing.is_visible()

    for address in [delivery, billing]:
        assert new_user["firstname"] in address.inner_text()
        assert new_user["lastname"] in address.inner_text()
        assert new_user["address1"] in address.inner_text()
        assert new_user["address2"] in address.inner_text()
        assert new_user["city"] in address.inner_text()
        assert new_user["state"] in address.inner_text()
        assert new_user["zipcode"] in address.inner_text()
        assert new_user["country"] in address.inner_text()
        assert new_user["mobile_number"] in address.inner_text()

    # Verify Review Your Order
    assert app.checkout.order_review.is_visible()
    assert product_name in app.checkout.order_review.inner_text()

    # Steps 12–15: Place order, pay, and verify confirmation
    place_order_and_pay(app, card, "Test comment")

    # Steps 16–17: Delete account and verify deletion
    delete_account_through_ui(app)
