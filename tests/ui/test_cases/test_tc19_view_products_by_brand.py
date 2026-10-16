"""Test Case 19 View & Cart Brand Products.

See https://automationexercise.com/test_cases
"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]

@pytest.mark.parametrize(
    "brand, section_title",
    [
        ("Polo", "Brand - Polo Products"),
        ("H&M", "Brand - H&M Products"),
        ("Madame", "Brand - Madame Products"),
        ("Mast & Harbour", "Brand - Mast & Harbour Products"),
        ("Babyhug", "Brand - Babyhug Products"),
        ("Allen Solly Junior", "Brand - Allen Solly Junior Products"),
        ("Kookie Kids", "Brand - Kookie Kids Products"),
        ("Biba", "Brand - Biba Products"),
    ],
)
def test_tc19_view_products_by_brand(app, brand, section_title):
    app.home.open()
    verify_home_page_visible(app)

    app.nav.products_link.click() 

    assert app.sidebar.brands_heading.is_visible()

    app.sidebar.open_brand(brand)
    assert section_title.lower() in app.home.section_title.inner_text().lower()