"""Test Case 8: Verify All Products and product detail page

See https://automationexercise.com/test_cases
"""

import pytest
from playwright.sync_api import expect

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc08_test_cases_page_is_opened(app):
    # Launch browser and open the site
    app.home.open()                           
    # Verify Home Page is visible                
    verify_home_page_visible(app)                             
    # Click on Signup/Login button
    app.nav.products_link.click() 
    # Verify user is navigated to ALL PRODUCTS page successfully
    assert app.products.heading.is_visible()
    # Verify that list of products is visible
    # Verify that the list of products is visible
    expect(app.products.cards.first).to_be_visible()
    assert app.products.cards.count() > 1
    # Click on 'View Product' of first product
    # Click on 'View Product' of first product
    app.products.cards.first.get_by_role("link", name="View Product").click()
    # User is landed to product detail page
    assert app.product_detail.info.is_visible()  
    # Verify that detail is visible: product name, category, price, availability, condition, brand
    assert app.product_detail.name.is_visible()
    assert app.product_detail.price.is_visible()

