"""Test Case 6: Contact Us Form.

See https://automationexercise.com/test_cases
"""

from pathlib import Path

import pytest
from playwright.sync_api import expect

from tests.ui.test_cases.steps import verify_home_page_visible

file_path = (
    Path(__file__).resolve().parents[2]
    / "test_data"
    / "files"
    / "test_file.txt"
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc06_contact_us_form(app):
    app.home.open()
    # Verify Home Page is visible
    verify_home_page_visible(app)
    # Click on Contact Us button
    app.nav.contact_link.click()
    app.page.wait_for_load_state("networkidle")
    # Verify "Get In Touch" heading is visible
    assert app.contact.heading.is_visible()
    # Fill out the form and click Submit button
    app.contact.submit(
        "Test User",
        "test@example.com",
        "Website Feedback",
        "This is a test message",
        file_path,
    )
    # Verify success message is visible
    expect(app.contact.success_message).to_contain_text(
        "Success! Your details have been submitted successfully."
    )
    # Click Home button
    app.contact.home_button.click()
    # Verify Home Page is visible
    verify_home_page_visible(app)