"""Test Case 19 View & Cart Brand Products.

See https://automationexercise.com/test_cases
"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]

def test_tc19_view_products_by_brand(app):
    app.home.open()
    verify_home_page_visible(app)

    app.nav.products_link.click() 

    assert app.sidebar.brands_heading.is_visible()

    app.sidebar.open_brand("Polo")
    assert "Brand - Polo Products" in app.home.section_title.inner_text() 