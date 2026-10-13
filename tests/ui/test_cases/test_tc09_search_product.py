"""Test Case 9 Search product.

See https://automationexercise.com/test_cases
"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc09_search_product(app):
    app.home.open()
    verify_home_page_visible(app)
    app.nav.products_link.click()
    assert app.products.heading.is_visible()
