"""
Fixtures Layer - Dependency Injection
Professional teams use fixtures to provide ready-to-use objects to tests
"""
import pytest
from playwright.sync_api import Page, Browser, sync_playwright
from tests.pages.app_pages import (
    HomePage, LoginPage, RegisterPage, ProductsPage, 
    CheckoutPage, DashboardPage
)
from tests.components.common_components import NavigationComponent

@pytest.fixture(scope="session")
def browser():
    """Browser instance for the test session"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser: Browser):
    """New page for each test"""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def home_page(page: Page):
    """Home page fixture"""
    return HomePage(page)

@pytest.fixture
def login_page(page: Page):
    """Login page fixture"""
    return LoginPage(page)

@pytest.fixture
def register_page(page: Page):
    """Register page fixture"""
    return RegisterPage(page)

@pytest.fixture
def products_page(page: Page):
    """Products page fixture"""
    return ProductsPage(page)

@pytest.fixture
def checkout_page(page: Page):
    """Checkout page fixture"""
    return CheckoutPage(page)

@pytest.fixture
def dashboard_page(page: Page):
    """Dashboard page fixture"""
    return DashboardPage(page)

@pytest.fixture
def navigation(page: Page):
    """Navigation component fixture"""
    return NavigationComponent(page)

@pytest.fixture
def authenticated_page(page: Page, login_page: LoginPage):
    """
    Fixture that provides an already authenticated page
    Useful for tests that require login state
    """
    login_page.navigate()
    login_page.login("testuser", "password123")
    page.wait_for_url("**/dashboard")
    return page

@pytest.fixture
def admin_authenticated_page(page: Page, login_page: LoginPage):
    """
    Fixture that provides an authenticated admin page
    """
    login_page.navigate()
    login_page.login("admin", "admin123")
    page.wait_for_url("**/dashboard")
    return page

@pytest.fixture(autouse=True)
def clear_local_storage(page: Page):
    """
    Auto-use fixture to clear local storage before each test
    Ensures clean state
    """
    yield  # Run the test first
    # Cleanup after test
    try:
        page.evaluate("() => localStorage.clear()")
    except:
        pass  # Page might be closed already
