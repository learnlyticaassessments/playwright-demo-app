"""
Page Object Model - Business API Layer
Pages expose business actions, hiding implementation details
"""
from playwright.sync_api import Page, expect
from tests.locators.app_locators import (
    LoginLocators, RegisterLocators, HomeLocators, 
    ProductsLocators, CheckoutLocators, DashboardLocators
)

class BasePage:
    """Base page with common functionality"""
    
    def __init__(self, page: Page):
        self.page = page
        
    def goto(self, url: str):
        """Navigate to URL"""
        self.page.goto(url)
        
    def wait_for_load_state(self):
        """Wait for page to load"""
        self.page.wait_for_load_state("networkidle")

class HomePage(BasePage):
    """Home page business API"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.base_url = "http://localhost:5000"
        
    def navigate(self):
        """Go to home page"""
        self.goto(self.base_url)
        
    def click_shop_now(self):
        """Click main shop now button"""
        self.page.get_by_test_id(HomeLocators.SHOP_NOW_BUTTON).click()
        
    def click_register(self):
        """Click register button"""
        self.page.get_by_test_id(HomeLocators.REGISTER_BUTTON).click()
        
    def subscribe_to_newsletter(self, email: str):
        """Subscribe to newsletter"""
        self.page.get_by_test_id(HomeLocators.NEWSLETTER_EMAIL_INPUT).fill(email)
        self.page.get_by_test_id(HomeLocators.NEWSLETTER_SUBSCRIBE_BUTTON).click()
        
    def get_newsletter_message(self) -> str:
        """Get newsletter subscription message"""
        self.page.get_by_test_id(HomeLocators.NEWSLETTER_MESSAGE).wait_for(state="visible")
        return self.page.get_by_test_id(HomeLocators.NEWSLETTER_MESSAGE).text_content()
        
    def is_hero_visible(self) -> bool:
        """Check if hero section is visible"""
        return self.page.get_by_test_id(HomeLocators.HERO_SECTION).is_visible()

class LoginPage(BasePage):
    """Login page business API"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.base_url = "http://localhost:5000/login"
        
    def navigate(self):
        """Go to login page"""
        self.goto(self.base_url)
        
    def login(self, username: str, password: str, remember_me: bool = False):
        """Perform login action"""
        self.page.get_by_test_id(LoginLocators.USERNAME_INPUT).fill(username)
        self.page.get_by_test_id(LoginLocators.PASSWORD_INPUT).fill(password)
        
        if remember_me:
            self.page.get_by_test_id(LoginLocators.REMEMBER_CHECKBOX).check()
            
        self.page.get_by_test_id(LoginLocators.SUBMIT_LOGIN_BUTTON).click()
        
    def get_error_message(self) -> str:
        """Get login error message"""
        self.page.get_by_test_id(LoginLocators.ERROR_MESSAGE).wait_for(state="visible")
        return self.page.get_by_test_id(LoginLocators.ERROR_MESSAGE).text_content()
        
    def click_register_link(self):
        """Click register link"""
        self.page.get_by_test_id(LoginLocators.REGISTER_LINK).click()
        
    def is_login_page_displayed(self) -> bool:
        """Check if on login page"""
        return self.page.get_by_test_id(LoginLocators.LOGIN_CONTAINER).is_visible()

class RegisterPage(BasePage):
    """Registration page business API"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.base_url = "http://localhost:5000/register"
        
    def navigate(self):
        """Go to register page"""
        self.goto(self.base_url)
        
    def register(self, username: str, email: str, password: str, 
                 confirm_password: str, accept_terms: bool = True):
        """Perform registration"""
        self.page.get_by_test_id(RegisterLocators.REGISTER_USERNAME_INPUT).fill(username)
        self.page.get_by_test_id(RegisterLocators.REGISTER_EMAIL_INPUT).fill(email)
        self.page.get_by_test_id(RegisterLocators.REGISTER_PASSWORD_INPUT).fill(password)
        self.page.get_by_test_id(RegisterLocators.REGISTER_CONFIRM_PASSWORD_INPUT).fill(confirm_password)
        
        if accept_terms:
            self.page.get_by_test_id(RegisterLocators.TERMS_CHECKBOX).check()
            
        self.page.get_by_test_id(RegisterLocators.SUBMIT_REGISTER_BUTTON).click()
        
    def get_error_message(self) -> str:
        """Get registration error message"""
        self.page.get_by_test_id(RegisterLocators.REGISTER_ERROR_MESSAGE).wait_for(state="visible")
        return self.page.get_by_test_id(RegisterLocators.REGISTER_ERROR_MESSAGE).text_content()
        
    def get_success_message(self) -> str:
        """Get registration success message"""
        self.page.get_by_test_id(RegisterLocators.REGISTER_SUCCESS_MESSAGE).wait_for(state="visible")
        return self.page.get_by_test_id(RegisterLocators.REGISTER_SUCCESS_MESSAGE).text_content()

class ProductsPage(BasePage):
    """Products page business API"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.base_url = "http://localhost:5000/products"
        
    def navigate(self):
        """Go to products page"""
        self.goto(self.base_url)
        
    def filter_by_category(self, category: str):
        """Filter products by category"""
        self.page.get_by_test_id(ProductsLocators.CATEGORY_FILTER).select_option(category)
        
    def search_products(self, search_term: str):
        """Search for products"""
        self.page.get_by_test_id(ProductsLocators.SEARCH_INPUT).fill(search_term)
        
    def clear_filters(self):
        """Clear all filters"""
        self.page.get_by_test_id(ProductsLocators.CLEAR_FILTERS_BUTTON).click()
        
    def add_product_to_cart(self, product_id: int):
        """Add product to cart"""
        self.page.get_by_test_id(f"add-to-cart-{product_id}").click()
        
    def view_product_details(self, product_id: int):
        """View product details"""
        self.page.get_by_test_id(f"view-details-{product_id}").click()
        
    def get_product_count(self) -> int:
        """Get number of displayed products"""
        self.page.get_by_test_id(ProductsLocators.LOADING_INDICATOR).wait_for(state="hidden", timeout=5000)
        products = self.page.get_by_test_id(ProductsLocators.PRODUCTS_GRID).locator('[data-testid^="product-"]').all()
        return len(products)
        
    def is_no_products_message_shown(self) -> bool:
        """Check if no products message is displayed"""
        return self.page.get_by_test_id(ProductsLocators.NO_PRODUCTS_MESSAGE).is_visible()

class CheckoutPage(BasePage):
    """Checkout page business API"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.base_url = "http://localhost:5000/checkout"
        
    def navigate(self):
        """Go to checkout page"""
        self.goto(self.base_url)
        
    def fill_shipping_info(self, address: str, city: str):
        """Fill shipping information"""
        self.page.get_by_test_id(CheckoutLocators.SHIPPING_ADDRESS_INPUT).fill(address)
        self.page.get_by_test_id(CheckoutLocators.SHIPPING_CITY_INPUT).fill(city)
        
    def accept_terms(self):
        """Accept terms and conditions"""
        self.page.get_by_test_id(CheckoutLocators.ACCEPT_TERMS_CHECKBOX).check()
        
    def place_order(self):
        """Place the order"""
        self.page.get_by_test_id(CheckoutLocators.PLACE_ORDER_BUTTON).click()
        
    def complete_checkout(self, address: str, city: str):
        """Complete full checkout process"""
        self.fill_shipping_info(address, city)
        self.accept_terms()
        self.place_order()
        
    def get_checkout_message(self) -> str:
        """Get checkout message"""
        self.page.get_by_test_id(CheckoutLocators.CHECKOUT_MESSAGE).wait_for(state="visible")
        return self.page.get_by_test_id(CheckoutLocators.CHECKOUT_MESSAGE).text_content()

class DashboardPage(BasePage):
    """Dashboard page business API"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.base_url = "http://localhost:5000/dashboard"
        
    def navigate(self):
        """Go to dashboard page"""
        self.goto(self.base_url)
        
    def is_admin_badge_visible(self) -> bool:
        """Check if admin badge is displayed"""
        try:
            return self.page.get_by_test_id(DashboardLocators.ADMIN_BADGE).is_visible()
        except:
            return False
            
    def view_profile(self):
        """Go to profile page"""
        self.page.get_by_test_id(DashboardLocators.VIEW_PROFILE_LINK).click()
        
    def logout(self):
        """Logout from dashboard"""
        self.page.get_by_test_id(DashboardLocators.LOGOUT_BUTTON).click()
