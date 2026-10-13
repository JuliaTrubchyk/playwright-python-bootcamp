"""Test Case 5: Register user with an existing email.

See https://automationexercise.com/test_cases
"""

import re

import pytest

from tests.ui.test_cases.steps import (
    verify_home_page_visible
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc05_register_user_with_existing_email(app, new_user):
    # Launch browser and open the site
    app.home.open()                           
    # Verify Home Page is visible                
    verify_home_page_visible(app)                             
    # Click on Signup/Login button
    app.nav.login_link.click()                               
    # Verify "New User Signup!" heading is visible
    assert app.login.signup_heading.inner_text() == "New User Signup!"    
    # Enter name an already registered email address
    app.login.start_signup(new_user["name"], new_user["email"])
    # Verify "Email Address already exist!" message is displayed
    assert app.login.signup_error.is_visible()
