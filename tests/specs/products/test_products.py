"""
Products Tests
Demonstrates: Dynamic content locators, filtering, list operations, chaining
"""
import pytest
from playwright.sync_api import expect
from tests.pages.app_pages import ProductsPage
import re

def test_products_page_loads_successfully(products_page: ProductsPage):
    """
    Demonstrates: Page load verification
    Best Practice: Verify key elements are present
    """
    # GIVEN/WHEN: User navigates to products page
    products_page.navigate()
    
    # THEN: Products are loaded and displayed
    products_page.page.get_by_test_id("loading-indicator").wait_for(state="hidden")
    product_count = products_page.get_product_count()
    assert product_count > 0, "Products should be loaded"

def test_filter_products_by_category(products_page: ProductsPage):
    """
    Demonstrates: Select dropdown locators
    Shows: Filtering dynamic content
    """
    # GIVEN: User is on products page
    products_page.navigate()
    products_page.page.get_by_test_id("loading-indicator").wait_for(state="hidden")
    
    # Get initial product count
    initial_count = products_page.get_product_count()
    
    # WHEN: User filters by Electronics category
    products_page.filter_by_category("Electronics")
    products_page.page.get_by_test_id("loading-indicator").wait_for(state="hidden")
    
    # THEN: Filtered products are shown
    filtered_count = products_page.get_product_count()
    assert filtered_count < initial_count, "Filter should reduce product count"

def test_search_products_by_name(products_page: ProductsPage):
    """
    Demonstrates: Text input locators
    Shows: Search functionality with dynamic results
    """
    # GIVEN: User is on products page
    products_page.navigate()
    products_page.page.get_by_test_id("loading-indicator").wait_for(state="hidden")
    
    # WHEN: User searches for "laptop"
    products_page.search_products("laptop")
    products_page.page.wait_for_timeout(500)  # Debounce delay
    products_page.page.get_by_test_id("loading-indicator").wait_for(state="hidden")
    
    # THEN: Only matching products are shown
    product_count = products_page.get_product_count()
    assert product_count >= 1, "Should find laptop products"

def test_clear_filters_resets_products(products_page: ProductsPage):
    """
    Demonstrates: Button click actions
    Shows: State reset functionality
    """
    # GIVEN: User has applied filters
    products_page.navigate()
    products_page.page.get_by_test_id("loading-indicator").wait_for(state="hidden")
    initial_count = products_page.get_product_count()
    
    products_page.filter_by_category("Accessories")
    products_page.page.get_by_test_id("loading-indicator").wait_for(state="hidden")
    
    # WHEN: User clears filters
    products_page.clear_filters()
    products_page.page.get_by_test_id("loading-indicator").wait_for(state="hidden")
    
    # THEN: All products are shown again
    final_count = products_page.get_product_count()
    assert final_count == initial_count

def test_add_product_to_cart(products_page: ProductsPage, navigation):
    """
    Demonstrates: Dynamic test ID locators with variables
    Shows: Cart count updates
    """
    # GIVEN: User is on products page
    products_page.navigate()
    products_page.page.get_by_test_id("loading-indicator").wait_for(state="hidden")
    
    initial_cart_count = navigation.get_cart_count()
    
    # WHEN: User adds first product to cart
    products_page.add_product_to_cart(1)
    
    # Wait for the "Added" feedback
    products_page.page.wait_for_timeout(500)
    
    # THEN: Cart count increases
    new_cart_count = navigation.get_cart_count()
    assert int(new_cart_count) == int(initial_cart_count) + 1

def test_view_product_details(products_page: ProductsPage, page):
    """
    Demonstrates: Navigation to detail page
    Shows: Link locators with dynamic IDs
    """
    # GIVEN: User is on products page
    products_page.navigate()
    products_page.page.get_by_test_id("loading-indicator").wait_for(state="hidden")
    
    # WHEN: User clicks view details for product 1
    products_page.view_product_details(1)
    
    # THEN: User is on product detail page
    expect(page).to_have_url(re.compile(r"/product/1"))
    expect(page.get_by_test_id("product-detail-name")).to_be_visible()

def test_no_products_message_when_no_matches(products_page: ProductsPage):
    """
    Demonstrates: Conditional element visibility
    Shows: Empty state handling
    """
    # GIVEN: User is on products page
    products_page.navigate()
    products_page.page.get_by_test_id("loading-indicator").wait_for(state="hidden")
    
    # WHEN: User searches for non-existent product
    products_page.search_products("xyznonexistent")
    products_page.page.wait_for_timeout(500)
    products_page.page.get_by_test_id("loading-indicator").wait_for(state="hidden")
    
    # THEN: No products message is shown
    assert products_page.is_no_products_message_shown()

def test_product_card_displays_correct_info(page):
    """
    Demonstrates: Accessing nested elements with locator chaining
    Shows: Data verification in complex components
    """
    # GIVEN: User is on products page
    page.goto("http://localhost:5000/products")
    page.get_by_test_id("loading-indicator").wait_for(state="hidden")
    
    # WHEN: Examining first product
    first_product = page.get_by_test_id("product-1")
    
    # THEN: Product card has all required information
    expect(first_product.get_by_test_id("product-name-1")).to_be_visible()
    expect(first_product.get_by_test_id("product-price-1")).to_contain_text("$")
    expect(first_product.get_by_test_id("product-stock-1")).to_contain_text("in stock")
    expect(first_product.get_by_test_id("product-category-1")).to_be_visible()

def test_products_grid_uses_role_list(page):
    """
    Demonstrates: ARIA role locators
    Shows: Accessibility-first approach
    """
    # GIVEN: User is on products page
    page.goto("http://localhost:5000/products")
    page.get_by_test_id("loading-indicator").wait_for(state="hidden")
    
    # WHEN: Checking products grid structure
    products_grid = page.get_by_test_id("products-grid")
    
    # THEN: Grid has proper role
    expect(products_grid).to_have_attribute("role", "list")
    
    # Each product card has role="listitem"
    first_product = page.get_by_test_id("product-1")
    expect(first_product).to_have_attribute("role", "listitem")
