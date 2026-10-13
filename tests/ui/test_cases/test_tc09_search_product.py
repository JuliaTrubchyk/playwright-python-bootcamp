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

    app.products.search("top")
    assert app.products.searched_heading.is_visible() 

    names = app.products.names.all()

    assert len(names) > 0

    for name in names:
        assert name.is_visible()

    