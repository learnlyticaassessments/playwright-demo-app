"""
Component Layer - Reusable UI Components
These components can appear in multiple pages
"""
from playwright.sync_api import Page
from tests.locators.app_locators import NavigationLocators

class NavigationComponent:
    """Navigation bar component that appears on all pages"""
    
    def __init__(self, page: Page):
        self.page = page
        
    def navigate_to_home(self):
        """Navigate to home page"""
        self.page.get_by_test_id(NavigationLocators.NAV_HOME).click()
        
    def navigate_to_products(self):
        """Navigate to products page"""
        self.page.get_by_test_id(NavigationLocators.NAV_PRODUCTS).click()
        
    def navigate_to_forms(self):
        """Navigate to forms demo page"""
        self.page.get_by_test_id(NavigationLocators.NAV_FORMS).click()
        
    def navigate_to_components(self):
        """Navigate to components demo page"""
        self.page.get_by_test_id(NavigationLocators.NAV_COMPONENTS).click()
        
    def go_to_cart(self):
        """Go to shopping cart"""
        self.page.get_by_test_id(NavigationLocators.CART_LINK).click()
        
    def go_to_login(self):
        """Go to login page"""
        self.page.get_by_test_id(NavigationLocators.LOGIN_BUTTON).click()
        
    def get_cart_count(self) -> str:
        """Get current cart item count"""
        return self.page.get_by_test_id(NavigationLocators.CART_COUNT).text_content()
        
    def click_logo(self):
        """Click logo to go home"""
        self.page.get_by_test_id(NavigationLocators.LOGO_LINK).click()

class ModalComponent:
    """Reusable modal dialog component"""
    
    def __init__(self, page: Page, modal_testid: str):
        self.page = page
        self.modal_testid = modal_testid
        
    def is_visible(self) -> bool:
        """Check if modal is visible"""
        modal = self.page.get_by_test_id(self.modal_testid)
        return modal.is_visible()
        
    def close(self):
        """Close the modal"""
        # Could use close button or cancel button
        close_btn = self.page.get_by_test_id("close-modal-button")
        if close_btn.is_visible():
            close_btn.click()
            
    def confirm(self):
        """Click confirm button"""
        self.page.get_by_test_id("modal-confirm-button").click()
        
    def cancel(self):
        """Click cancel button"""
        self.page.get_by_test_id("modal-cancel-button").click()
        
    def get_message(self) -> str:
        """Get modal message text"""
        return self.page.get_by_test_id("modal-message").text_content()

class AlertComponent:
    """Alert/notification component"""
    
    def __init__(self, page: Page):
        self.page = page
        
    def wait_for_alert(self, alert_type: str, timeout: int = 5000):
        """Wait for alert to appear"""
        self.page.get_by_test_id(f"alert-{alert_type}").wait_for(timeout=timeout)
        
    def get_alert_text(self, alert_type: str) -> str:
        """Get alert message text"""
        return self.page.get_by_test_id(f"alert-{alert_type}").text_content()
        
    def is_alert_visible(self, alert_type: str) -> bool:
        """Check if alert is visible"""
        try:
            return self.page.get_by_test_id(f"alert-{alert_type}").is_visible()
        except:
            return False

class FormValidationComponent:
    """Form validation messaging component"""
    
    def __init__(self, page: Page):
        self.page = page
        
    def get_error_message(self, message_testid: str = "error-message") -> str:
        """Get error message text"""
        return self.page.get_by_test_id(message_testid).text_content()
        
    def get_success_message(self, message_testid: str = "success-message") -> str:
        """Get success message text"""
        return self.page.get_by_test_id(message_testid).text_content()
        
    def is_error_visible(self, message_testid: str = "error-message") -> bool:
        """Check if error message is visible"""
        return self.page.get_by_test_id(message_testid).is_visible()
        
    def is_success_visible(self, message_testid: str = "success-message") -> bool:
        """Check if success message is visible"""
        return self.page.get_by_test_id(message_testid).is_visible()
