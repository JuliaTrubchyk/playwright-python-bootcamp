"""Test Case 18 View category products.

See https://automationexercise.com/test_cases
"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]

@pytest.mark.parametrize(
    "category, subcategory,section_title",
    [
        ("Women", "Dress", "Women - Dress Products"),
        ("Men", "Jeans", "Men - Jeans Products"),
        ("Kids", "Dress","Kids - Dress Products")
    ],
)
def test_tc18_view_categories(app, category, subcategory, section_title):
    app.home.open()
    verify_home_page_visible(app)

    assert app.sidebar.categories_heading.is_visible()
    app.sidebar.open_category(category)
    app.sidebar.open_subcategory(category, subcategory)

    assert section_title in app.home.section_title.inner_text()
