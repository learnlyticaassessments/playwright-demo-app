"""
Locator Contract Layer
Centralized locator definitions for maintainability
"""

class HomeLocators:
    """Locators for home page"""
    HERO_SECTION = "hero-section"
    SHOP_NOW_BUTTON = "shop-now-button"
    REGISTER_BUTTON = "register-button"
    FEATURES_SECTION = "features-section"
    NEWSLETTER_EMAIL_INPUT = "newsletter-email-input"
    NEWSLETTER_SUBSCRIBE_BUTTON = "newsletter-subscribe-button"
    NEWSLETTER_MESSAGE = "newsletter-message"
    
class LoginLocators:
    """Locators for login page"""
    LOGIN_CONTAINER = "login-container"
    USERNAME_INPUT = "username-input"
    PASSWORD_INPUT = "password-input"
    REMEMBER_CHECKBOX = "remember-checkbox"
    SUBMIT_LOGIN_BUTTON = "submit-login-button"
    ERROR_MESSAGE = "error-message"
    REGISTER_LINK = "register-link"
    FORGOT_PASSWORD_LINK = "forgot-password-link"

class RegisterLocators:
    """Locators for registration page"""
    REGISTER_CONTAINER = "register-container"
    REGISTER_USERNAME_INPUT = "register-username-input"
    REGISTER_EMAIL_INPUT = "register-email-input"
    REGISTER_PASSWORD_INPUT = "register-password-input"
    REGISTER_CONFIRM_PASSWORD_INPUT = "register-confirm-password-input"
    TERMS_CHECKBOX = "terms-checkbox"
    SUBMIT_REGISTER_BUTTON = "submit-register-button"
    REGISTER_ERROR_MESSAGE = "register-error-message"
    REGISTER_SUCCESS_MESSAGE = "register-success-message"

class ProductsLocators:
    """Locators for products page"""
    PRODUCTS_CONTAINER = "products-container"
    CATEGORY_FILTER = "category-filter"
    SEARCH_INPUT = "search-input"
    CLEAR_FILTERS_BUTTON = "clear-filters-button"
    PRODUCTS_GRID = "products-grid"
    LOADING_INDICATOR = "loading-indicator"
    NO_PRODUCTS_MESSAGE = "no-products-message"

class CheckoutLocators:
    """Locators for checkout page"""
    CHECKOUT_CONTAINER = "checkout-container"
    SHIPPING_ADDRESS_INPUT = "shipping-address-input"
    SHIPPING_CITY_INPUT = "shipping-city-input"
    ACCEPT_TERMS_CHECKBOX = "accept-terms-checkbox"
    PLACE_ORDER_BUTTON = "place-order-button"
    CHECKOUT_MESSAGE = "checkout-message"

class NavigationLocators:
    """Locators for navigation"""
    NAV_HOME = "nav-home"
    NAV_PRODUCTS = "nav-products"
    NAV_FORMS = "nav-forms"
    NAV_COMPONENTS = "nav-components"
    CART_LINK = "cart-link"
    CART_COUNT = "cart-count"
    LOGIN_BUTTON = "login-button"
    LOGO_LINK = "logo-link"
    LOCALE_SWITCHER = "locale-switcher"
    LOCALE_EN = "locale-en"
    LOCALE_ES = "locale-es"

class DashboardLocators:
    """Locators for dashboard"""
    DASHBOARD_CONTAINER = "dashboard-container"
    ADMIN_BADGE = "admin-badge"
    ORDERS_CARD = "orders-card"
    PROFILE_CARD = "profile-card"
    VIEW_PROFILE_LINK = "view-profile-link"
    LOGOUT_BUTTON = "logout-button"

class FormsLocators:
    """Locators for forms demo page"""
    FORMS_DEMO_CONTAINER = "forms-demo-container"
    FIRST_NAME_INPUT = "first-name-input"
    LAST_NAME_INPUT = "last-name-input"
    EMAIL_DEMO_INPUT = "email-demo-input"
    COUNTRY_SELECT = "country-select"
    SIZE_SMALL_RADIO = "size-small-radio"
    SIZE_MEDIUM_RADIO = "size-medium-radio"
    SIZE_LARGE_RADIO = "size-large-radio"
    NEWSLETTER_CHECKBOX = "newsletter-checkbox"
    PROMOTIONS_CHECKBOX = "promotions-checkbox"
    BIRTH_DATE_INPUT = "birth-date-input"
    COMMENTS_TEXTAREA = "comments-textarea"
    FILE_UPLOAD_INPUT = "file-upload-input"
    REQUIRED_FIELD_INPUT = "required-field-input"
    VALIDATION_MESSAGE = "validation-message"
    SUBMIT_VALIDATION_FORM = "submit-validation-form"
    
    # Multi-step form
    MULTISTEP_FORM = "multistep-form"
    STEP_INDICATOR_1 = "step-indicator-1"
    STEP_INDICATOR_2 = "step-indicator-2"
    STEP_INDICATOR_3 = "step-indicator-3"
    STEP_1 = "step-1"
    STEP1_NAME_INPUT = "step1-name-input"
    NEXT_STEP_1 = "next-step-1"
    STEP_2 = "step-2"
    STEP2_PHONE_INPUT = "step2-phone-input"
    PREV_STEP_2 = "prev-step-2"
    NEXT_STEP_2 = "next-step-2"
    STEP_3 = "step-3"
    PREV_STEP_3 = "prev-step-3"
    SUBMIT_MULTISTEP = "submit-multistep"
    MULTISTEP_SUCCESS = "multistep-success"

class ComponentsLocators:
    """Locators for components demo page"""
    COMPONENTS_DEMO_CONTAINER = "components-demo-container"
    
    # Modal
    OPEN_MODAL_BUTTON = "open-modal-button"
    DEMO_MODAL = "demo-modal"
    CLOSE_MODAL_BUTTON = "close-modal-button"
    MODAL_CANCEL_BUTTON = "modal-cancel-button"
    MODAL_CONFIRM_BUTTON = "modal-confirm-button"
    MODAL_MESSAGE = "modal-message"
    
    # Dropdown
    DROPDOWN_TOGGLE_BUTTON = "dropdown-toggle-button"
    DROPDOWN_MENU = "dropdown-menu"
    DROPDOWN_OPTION_1 = "dropdown-option-1"
    DROPDOWN_OPTION_2 = "dropdown-option-2"
    SELECTED_OPTION = "selected-option"
    
    # Tabs
    TABS_CONTAINER = "tabs-container"
    TAB_PROFILE = "tab-profile"
    TAB_SETTINGS = "tab-settings"
    TAB_NOTIFICATIONS = "tab-notifications"
    TAB_PANEL_PROFILE = "tab-panel-profile"
    TAB_PANEL_SETTINGS = "tab-panel-settings"
    TAB_PANEL_NOTIFICATIONS = "tab-panel-notifications"
    
    # Alerts
    SHOW_SUCCESS_ALERT = "show-success-alert"
    SHOW_ERROR_ALERT = "show-error-alert"
    SHOW_WARNING_ALERT = "show-warning-alert"
    ALERTS_CONTAINER = "alerts-container"
    
    # Accordion
    ACCORDION_HEADER_1 = "accordion-header-1"
    ACCORDION_CONTENT_1 = "accordion-content-1"
    ACCORDION_HEADER_2 = "accordion-header-2"
    ACCORDION_CONTENT_2 = "accordion-content-2"
    
    # Data Table
    DATA_TABLE = "data-table"
    TABLE_HEADER_NAME = "table-header-name"
    TABLE_ROW_1 = "table-row-1"
    EDIT_ROW_1 = "edit-row-1"
    DELETE_ROW_1 = "delete-row-1"
    
    # Progress Bar
    PROGRESS_BAR = "progress-bar"
    START_PROGRESS = "start-progress"
    PROGRESS_TEXT = "progress-text"
    
    # Toast
    SHOW_TOAST = "show-toast"
    TOAST_CONTAINER = "toast-container"
