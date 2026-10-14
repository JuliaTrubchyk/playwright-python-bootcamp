"""Test Case 18 View category products.

See https://automationexercise.com/test_cases
"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc18_view_categories(app):
    app.home.open()
    verify_home_page_visible(app)

    assert app.sidebar.categories_heading.is_visible()
    app.sidebar.open_category("Women")
    app.sidebar.open_subcategory("Women", "Tops")

    assert "Women - Tops Products" in app.home.section_title.inner_text()
