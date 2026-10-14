"""Test Case 15 Place order register before checkout.

See https://automationexercise.com/test_cases
"""


import pytest

from tests.ui.test_cases.steps import (
    delete_account_through_ui,
    place_order_and_pay,
    sign_up_through_ui,
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


def test_tc15_place_order_register_before_checkout(app, signup_user):
    app.home.open()
    verify_home_page_visible(app)
    
    app.nav.login_link.click()     

    # Steps 5-7: Create account and verify login
    sign_up_through_ui(app, signup_user)
    verify_logged_in_as(app, signup_user["name"])          

    # Steps 8–10: Add product and open cart
    product_name = app.home.featured_items.first.locator(".productinfo p").inner_text()
    app.home.add_card_to_cart(app.home.featured_items.first)
    app.home.view_cart_from_modal()
    assert app.page.url.endswith("/view_cart")         

    app.cart.proceed_to_checkout()

    # Step 12: Verify Address Details
    delivery = app.checkout.delivery_address
    billing = app.checkout.billing_address

    assert delivery.is_visible()
    assert billing.is_visible()

    for address in [delivery, billing]:
        assert signup_user["firstname"] in address.inner_text()
        assert signup_user["lastname"] in address.inner_text()
        assert signup_user["address1"] in address.inner_text()
        assert signup_user["address2"] in address.inner_text()
        assert signup_user["city"] in address.inner_text()
        assert signup_user["state"] in address.inner_text()
        assert signup_user["zipcode"] in address.inner_text()
        assert signup_user["country"] in address.inner_text()
        assert signup_user["mobile_number"] in address.inner_text()

    # Verify Review Your Order
    assert app.checkout.order_review.is_visible()
    assert product_name in app.checkout.order_review.inner_text()

    # Steps 13–15: Place order, pay, and verify confirmation
    place_order_and_pay(app, card, "Test comment")

    # Steps 17–18: Delete account and verify deletion
    delete_account_through_ui(app)


    