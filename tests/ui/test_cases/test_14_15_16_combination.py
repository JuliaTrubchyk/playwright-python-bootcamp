# TC 14: Add product → Start checkout → Register → Complete order.
# TC 15: Register → Add product → Complete order.
# TC 16: Log in → Add product → Complete order.

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

@pytest.mark.parametrize(
    "scenario, user_type",
    [
        ("tc14", "signup_user"),
        ("tc15", "signup_user"),
        ("tc16", "new_user"),
    ],
)
def test_14_15_16_combination(app, scenario, user_type, request):
    user = request.getfixturevalue(user_type)

    app.home.open()
    verify_home_page_visible(app)

    if scenario == "tc14":
        product_name = app.home.featured_items.first.locator(".productinfo p").inner_text()
        app.home.add_card_to_cart(app.home.featured_items.first)
        app.home.view_cart_from_modal()
        assert app.page.url.endswith("/view_cart")

        app.cart.proceed_to_checkout()
        app.cart.register_login_link.click()

        sign_up_through_ui(app, user)
        verify_logged_in_as(app, user["name"])

        app.nav.cart_link.click()
        app.cart.proceed_to_checkout()

    elif scenario == "tc15":
        app.nav.login_link.click()     

        sign_up_through_ui(app, user)
        verify_logged_in_as(app, user["name"])          

        product_name = app.home.featured_items.first.locator(".productinfo p").inner_text()
        app.home.add_card_to_cart(app.home.featured_items.first)
        app.home.view_cart_from_modal()
        assert app.page.url.endswith("/view_cart")         

        app.cart.proceed_to_checkout()

    elif scenario == "tc16":
        app.nav.login_link.click()

        app.login.login(user["email"], user["password"])
        verify_logged_in_as(app, user["name"]) 
        
        product_name = app.home.featured_items.first.locator(".productinfo p").inner_text()
        app.home.add_card_to_cart(app.home.featured_items.first)
        app.home.view_cart_from_modal()

        assert app.page.url.endswith("/view_cart")    
        assert product_name in app.cart.item_names.first.inner_text()
        app.cart.proceed_to_checkout()


    verify_address_and_review(app, user, product_name)
    place_order_and_pay(app, card, "Test comment")
    delete_account_through_ui(app)