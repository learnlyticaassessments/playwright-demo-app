"""
Authentication Tests
Demonstrates: Role-based locators, label locators, test ID locators
"""
import pytest
from playwright.sync_api import expect
from tests.pages.app_pages import LoginPage, RegisterPage, DashboardPage

def test_successful_login_with_test_ids(login_page: LoginPage, page):
    """
    Demonstrates: Test ID locators (get_by_test_id)
    Best Practice: Using test IDs for stable, deterministic element selection
    """
    # GIVEN: User is on login page
    login_page.navigate()
    
    # WHEN: User logs in with valid credentials
    login_page.login("testuser", "password123")
    
    # THEN: User is redirected to dashboard
    page.wait_for_url("**/dashboard")
    expect(page).to_have_url("http://localhost:5000/dashboard")
    
def test_login_with_invalid_credentials(login_page: LoginPage):
    """
    Demonstrates: Error message handling with test IDs
    Shows: How to verify error states
    """
    # GIVEN: User is on login page
    login_page.navigate()
    
    # WHEN: User tries to login with invalid credentials
    login_page.login("invaliduser", "wrongpassword")
    
    # THEN: Error message is displayed
    error_message = login_page.get_error_message()
    assert "Invalid username or password" in error_message

def test_login_with_role_based_locators(page):
    """
    Demonstrates: Role-based locators (get_by_role)
    Best Practice: Highest priority locator strategy
    Accessibility: Ensures form elements have proper ARIA roles
    """
    # GIVEN: User navigates to login page
    page.goto("http://localhost:5000/login")
    
    # WHEN: Using role-based locators to interact with form
    # Note: These work because our HTML has proper semantic structure
    page.get_by_label("Username").fill("testuser")
    page.get_by_label("Password").fill("password123")
    
    # Checkbox has role="checkbox"
    page.get_by_role("checkbox", name="Remember me").check()
    
    # Button has role="button"
    page.get_by_role("button", name="Sign In").click()
    
    # THEN: Login succeeds
    page.wait_for_url("**/dashboard")
    
def test_register_new_user(register_page: RegisterPage):
    """
    Demonstrates: Form filling with test ID locators
    Shows: Multi-field form interaction
    """
    # GIVEN: User is on registration page
    register_page.navigate()
    
    # WHEN: User fills registration form
    import time
    unique_username = f"testuser_{int(time.time())}"
    register_page.register(
        username=unique_username,
        email=f"{unique_username}@example.com",
        password="SecurePass123",
        confirm_password="SecurePass123",
        accept_terms=True
    )
    
    # THEN: Success message is displayed
    success_message = register_page.get_success_message()
    assert "Registration successful" in success_message

def test_register_with_mismatched_passwords(register_page: RegisterPage):
    """
    Demonstrates: Form validation and error handling
    """
    # GIVEN: User is on registration page
    register_page.navigate()
    
    # WHEN: User submits form with mismatched passwords
    register_page.register(
        username="newuser",
        email="new@example.com",
        password="password1",
        confirm_password="password2",
        accept_terms=True
    )
    
    # THEN: Error message is shown
    error_message = register_page.get_error_message()
    assert "Passwords do not match" in error_message

def test_login_remember_me_checkbox(page):
    """
    Demonstrates: Checkbox interaction with test IDs
    Shows: State verification for checkboxes
    """
    # GIVEN: User is on login page
    page.goto("http://localhost:5000/login")
    
    # WHEN: User checks remember me
    checkbox = page.get_by_test_id("remember-checkbox")
    checkbox.check()
    
    # THEN: Checkbox is checked
    expect(checkbox).to_be_checked()

def test_admin_login_shows_admin_badge(login_page: LoginPage, dashboard_page: DashboardPage):
    """
    Demonstrates: Role-based UI elements
    Shows: Conditional element visibility
    """
    # GIVEN: Admin logs in
    login_page.navigate()
    login_page.login("admin", "admin123")
    
    # WHEN: On dashboard
    dashboard_page.page.wait_for_url("**/dashboard")
    
    # THEN: Admin badge is visible
    assert dashboard_page.is_admin_badge_visible()

def test_navigation_links_on_login_page(page):
    """
    Demonstrates: Link locators with test IDs
    Shows: Navigation between pages
    """
    # GIVEN: User is on login page
    page.goto("http://localhost:5000/login")
    
    # WHEN: User clicks register link
    page.get_by_test_id("register-link").click()
    
    # THEN: User is on register page
    expect(page).to_have_url("http://localhost:5000/register")
