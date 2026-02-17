"""
UI Components Tests
Demonstrates: Modal, tabs, dropdown, accordion, tables, alerts
"""
import pytest
from playwright.sync_api import expect
import re

def test_modal_open_and_close(page):
    """
    Demonstrates: Modal interaction
    Shows: Visibility toggling
    """
    # GIVEN: User is on components page
    page.goto("http://localhost:5000/components")
    
    # Modal should not be visible initially
    modal = page.get_by_test_id("demo-modal")
    expect(modal).to_be_hidden()
    
    # WHEN: User opens modal
    page.get_by_test_id("open-modal-button").click()
    
    # THEN: Modal is visible
    expect(modal).to_be_visible()
    
    # WHEN: User closes modal
    page.get_by_test_id("close-modal-button").click()
    
    # THEN: Modal is hidden
    expect(modal).to_be_hidden()

def test_modal_confirm_action(page):
    """
    Demonstrates: Modal action buttons
    """
    # GIVEN: Modal is open
    page.goto("http://localhost:5000/components")
    page.get_by_test_id("open-modal-button").click()
    
    # WHEN: User clicks confirm (will trigger alert in real app)
    # page.get_by_test_id("modal-confirm-button").click()
    
    # THEN: Modal closes
    # expect(page.get_by_test_id("demo-modal")).to_be_hidden()

def test_dropdown_menu_interaction(page):
    """
    Demonstrates: Dropdown menu
    Shows: Menu toggle and option selection
    """
    # GIVEN: User is on components page
    page.goto("http://localhost:5000/components")
    
    # Dropdown menu initially hidden
    dropdown_menu = page.get_by_test_id("dropdown-menu")
    expect(dropdown_menu).to_be_hidden()
    
    # WHEN: User clicks dropdown toggle
    page.get_by_test_id("dropdown-toggle-button").click()
    
    # THEN: Menu is visible
    expect(dropdown_menu).to_be_visible()
    
    # WHEN: User selects option
    page.get_by_test_id("dropdown-option-1").click()
    
    # THEN: Selection is displayed
    expect(page.get_by_test_id("selected-option")).to_contain_text("Option 1")

def test_tabs_navigation(page):
    """
    Demonstrates: Tab navigation
    Shows: Role-based tab locators
    """
    # GIVEN: User is on components page
    page.goto("http://localhost:5000/components")
    
    # Profile tab is active by default
    expect(page.get_by_test_id("tab-panel-profile")).to_be_visible()
    
    # WHEN: User clicks Settings tab
    page.get_by_test_id("tab-settings").click()
    
    # THEN: Settings panel is visible
    expect(page.get_by_test_id("tab-panel-settings")).to_be_visible()
    expect(page.get_by_test_id("tab-panel-profile")).to_be_hidden()
    
    # WHEN: User clicks Notifications tab
    page.get_by_test_id("tab-notifications").click()
    
    # THEN: Notifications panel is visible
    expect(page.get_by_test_id("tab-panel-notifications")).to_be_visible()
    expect(page.get_by_test_id("tab-panel-settings")).to_be_hidden()

def test_tabs_with_role_locators(page):
    """
    Demonstrates: Using ARIA roles for tabs
    Shows: Accessibility-first approach
    """
    # GIVEN: User is on components page
    page.goto("http://localhost:5000/components")
    
    # WHEN: Using role locators for tabs
    settings_tab = page.get_by_role("tab", name="Settings")
    settings_tab.click()
    
    # THEN: Settings panel is visible
    settings_panel = page.get_by_role("tabpanel", name="tab-panel-settings")
    expect(settings_panel).to_be_visible()

def test_alert_notifications(page):
    """
    Demonstrates: Dynamic alert creation
    Shows: Temporary elements
    """
    # GIVEN: User is on components page
    page.goto("http://localhost:5000/components")
    
    # WHEN: User triggers success alert
    page.get_by_test_id("show-success-alert").click()
    
    # THEN: Success alert appears
    expect(page.get_by_test_id("alert-success")).to_be_visible()
    
    # WHEN: User triggers error alert
    page.get_by_test_id("show-error-alert").click()
    
    # THEN: Error alert appears
    expect(page.get_by_test_id("alert-error")).to_be_visible()

def test_accordion_expand_collapse(page):
    """
    Demonstrates: Accordion interaction
    Shows: Expand/collapse pattern
    """
    # GIVEN: User is on components page
    page.goto("http://localhost:5000/components")
    
    # Content is hidden initially
    expect(page.get_by_test_id("accordion-content-1")).to_be_hidden()
    
    # WHEN: User clicks accordion header
    page.get_by_test_id("accordion-header-1").click()
    
    # THEN: Content is visible
    expect(page.get_by_test_id("accordion-content-1")).to_be_visible()
    
    # WHEN: User clicks again
    page.get_by_test_id("accordion-header-1").click()
    
    # THEN: Content is hidden
    expect(page.get_by_test_id("accordion-content-1")).to_be_hidden()

def test_data_table_structure(page):
    """
    Demonstrates: Table locators with roles
    Shows: Table cell access
    """
    # GIVEN: User is on components page
    page.goto("http://localhost:5000/components")
    
    # WHEN: Examining table structure
    table = page.get_by_test_id("data-table")
    
    # THEN: Table has proper structure
    # Header uses role="columnheader"
    expect(table.get_by_role("columnheader", name="Name")).to_be_visible()
    
    # Rows use role="row"
    first_row = page.get_by_test_id("table-row-1")
    expect(first_row).to_be_visible()
    
    # Cells use role="cell"
    expect(first_row.get_by_role("cell").first).to_be_visible()

def test_data_table_row_actions(page):
    """
    Demonstrates: Action buttons in table rows
    Shows: Nested locators
    """
    # GIVEN: User is on components page
    page.goto("http://localhost:5000/components")
    
    # WHEN: Clicking edit button in first row
    edit_button = page.get_by_test_id("edit-row-1")
    expect(edit_button).to_be_visible()
    
    # AND: Delete button is also accessible
    delete_button = page.get_by_test_id("delete-row-1")
    expect(delete_button).to_be_visible()

def test_progress_bar(page):
    """
    Demonstrates: Progress bar with ARIA attributes
    Shows: Dynamic value updates
    """
    # GIVEN: User is on components page
    page.goto("http://localhost:5000/components")
    
    # Progress bar starts at 0
    progress_bar = page.get_by_test_id("progress-bar")
    expect(progress_bar).to_have_attribute("aria-valuenow", "0")
    
    # WHEN: User starts progress
    page.get_by_test_id("start-progress").click()
    
    # THEN: Progress updates (wait a bit for animation)
    page.wait_for_timeout(3000)
    
    # Progress text should show increase
    progress_text = page.get_by_test_id("progress-text").text_content()
    assert progress_text != "0%", "Progress should have advanced"

def test_toast_notification(page):
    """
    Demonstrates: Toast notification (temporary pop-up)
    Shows: Animated elements
    """
    # GIVEN: User is on components page
    page.goto("http://localhost:5000/components")
    
    # WHEN: User triggers toast
    page.get_by_test_id("show-toast").click()
    
    # THEN: Toast appears
    page.wait_for_timeout(200)  # Wait for animation
    toast = page.get_by_test_id("toast-notification")
    expect(toast).to_be_visible()

def test_table_filtering_by_status(page):
    """
    Demonstrates: Filtering table rows
    Shows: Filter with has_text
    """
    # GIVEN: User is on components page
    page.goto("http://localhost:5000/components")
    
    # WHEN: Finding all active users
    active_rows = (page
        .get_by_test_id("data-table")
        .get_by_role("row")
        .filter(has_text="Active"))
    
    # THEN: Multiple active users found
    count = active_rows.count()
    assert count >= 2, "Should have active users"

def test_dropdown_with_role_menu(page):
    """
    Demonstrates: Menu role for dropdown
    Shows: menuitem role for options
    """
    # GIVEN: User is on components page
    page.goto("http://localhost:5000/components")
    
    # WHEN: Opening dropdown
    page.get_by_test_id("dropdown-toggle-button").click()
    
    # THEN: Menu items are accessible via role
    menu = page.get_by_role("menu")
    expect(menu).to_be_visible()
    
    # Menu items have role="menuitem"
    option1 = menu.get_by_role("menuitem").first
    expect(option1).to_be_visible()
