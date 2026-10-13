"""Test Case 9 Search product.

See https://automationexercise.com/test_cases
"""

import re

import pytest

from tests.ui.test_cases.steps import (
    delete_account_through_ui,
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]

def test_tc09_search_product(app):
    app.home.open()
    verify_home_page_visible(app)
    app.nav.products_link.click()
    assert app.products.heading.is_visible()
