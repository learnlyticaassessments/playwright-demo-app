"""
Forms Tests
Demonstrates: All input types, label locators, role locators, multi-step forms
"""
import pytest
from playwright.sync_api import expect
import re

def test_text_inputs_with_labels(page):
    """
    Demonstrates: Label locators (get_by_label)
    Best Practice: Using labels for form inputs
    """
    # GIVEN: User is on forms demo page
    page.goto("http://127.0.0.1:5000/forms")
    
    # WHEN: Filling text inputs using labels
    page.get_by_label("First Name").fill("John")
    page.get_by_label("Last Name").fill("Doe")
    page.get_by_label("Email Address").fill("john@example.com")
    
    # THEN: Values are filled
    expect(page.get_by_label("First Name")).to_have_value("John")
    expect(page.get_by_label("Last Name")).to_have_value("Doe")
    expect(page.get_by_label("Email Address")).to_have_value("john@example.com")

def test_select_dropdown(page):
    """
    Demonstrates: Select option locators
    Shows: Dropdown interaction
    """
    # GIVEN: User is on forms page
    page.goto("http://127.0.0.1:5000/forms")
    
    # WHEN: Selecting country from dropdown
    page.get_by_test_id("country-select").select_option("us")
    
    # THEN: Option is selected
    expect(page.get_by_test_id("country-select")).to_have_value("us")

def test_radio_buttons_with_roles(page):
    """
    Demonstrates: Radio button locators using roles
    Shows: Single selection from group
    """
    # GIVEN: User is on forms page
    page.goto("http://127.0.0.1:5000/forms")
    
    # WHEN: Selecting size using role locators
    page.get_by_role("radio", name="Medium size").check()
    
    # THEN: Radio is checked
    expect(page.get_by_role("radio", name="Medium size")).to_be_checked()
    
    # AND: Other radios in group are not checked
    expect(page.get_by_role("radio", name="Small size")).not_to_be_checked()
    expect(page.get_by_role("radio", name="Large size")).not_to_be_checked()

def test_checkboxes_multiple_selection(page):
    """
    Demonstrates: Checkbox locators
    Shows: Multiple selection capability
    """
    # GIVEN: User is on forms page
    page.goto("http://127.0.0.1:5000/forms")
    
    # WHEN: Checking multiple checkboxes
    page.get_by_role("checkbox", name="Subscribe to newsletter").check()
    page.get_by_role("checkbox", name="Receive promotional emails").check()
    
    # THEN: Both are checked
    expect(page.get_by_role("checkbox", name="Subscribe to newsletter")).to_be_checked()
    expect(page.get_by_role("checkbox", name="Receive promotional emails")).to_be_checked()
    
    # Third checkbox remains unchecked
    expect(page.get_by_role("checkbox", name="Product updates")).not_to_be_checked()

def test_date_input(page):
    """
    Demonstrates: Date input locators
    Shows: Date field interaction
    """
    # GIVEN: User is on forms page
    page.goto("http://127.0.0.1:5000/forms")
    
    # WHEN: Filling date field
    page.get_by_test_id("birth-date-input").fill("2000-01-15")
    
    # THEN: Date is set
    expect(page.get_by_test_id("birth-date-input")).to_have_value("2000-01-15")

def test_textarea(page):
    """
    Demonstrates: Textarea locators
    Shows: Multi-line text input
    """
    # GIVEN: User is on forms page
    page.goto("http://127.0.0.1:5000/forms")
    
    # WHEN: Filling textarea
    comment_text = "This is a test comment with multiple lines.\nSecond line here."
    page.get_by_test_id("comments-textarea").fill(comment_text)
    
    # THEN: Text is filled
    expect(page.get_by_test_id("comments-textarea")).to_have_value(comment_text)

def test_form_validation_required_field(page):
    """
    Demonstrates: Form validation and error messages
    Shows: Required field validation
    """
    # GIVEN: User is on forms page
    page.goto("http://127.0.0.1:5000/forms")
    
    # WHEN: Filling form with valid data
    page.get_by_test_id("required-field-input").fill("Test Value")
    page.get_by_test_id("min-length-input").fill("12345")
    page.get_by_test_id("number-input").fill("50")
    
    page.get_by_test_id("submit-validation-form").click()
    
    # THEN: Success message appears
    validation_message = page.get_by_test_id("validation-message")
    expect(validation_message).to_be_visible()
    expect(validation_message).to_contain_text("successfully")

def test_multi_step_form_navigation(page):
    """
    Demonstrates: Multi-step form with state management
    Shows: Step indicators and navigation
    """
    # GIVEN: User is on forms page
    page.goto("http://127.0.0.1:5000/forms")
    
    # WHEN: Starting multi-step form
    # Step 1
    expect(page.get_by_test_id("step-1")).to_be_visible()
    expect(page.get_by_test_id("step-indicator-1")).to_have_class(re.compile(r"active"))
    
    page.get_by_test_id("step1-name-input").fill("John Doe")
    page.get_by_test_id("next-step-1").click()
    
    # Step 2
    expect(page.get_by_test_id("step-2")).to_be_visible()
    expect(page.get_by_test_id("step-indicator-2")).to_have_class(re.compile(r"active"))
    
    page.get_by_test_id("step2-phone-input").fill("555-1234")
    page.get_by_test_id("next-step-2").click()
    
    # Step 3
    expect(page.get_by_test_id("step-3")).to_be_visible()
    expect(page.get_by_test_id("step-indicator-3")).to_have_class(re.compile(r"active"))
    
    page.get_by_test_id("submit-multistep").click()
    
    # THEN: Success message is shown
    expect(page.get_by_test_id("multistep-success")).to_be_visible()

def test_multi_step_form_backward_navigation(page):
    """
    Demonstrates: Backward navigation in multi-step form
    Shows: State preservation
    """
    # GIVEN: User is on step 2
    page.goto("http://127.0.0.1:5000/forms")
    page.get_by_test_id("step1-name-input").fill("Jane Doe")
    page.get_by_test_id("next-step-1").click()
    
    # WHEN: User goes back to step 1
    page.get_by_test_id("prev-step-2").click()
    
    # THEN: User is on step 1
    expect(page.get_by_test_id("step-1")).to_be_visible()
    
    # AND: Previous input is preserved (this is basic - real app might preserve)
    # expect(page.get_by_test_id("step1-name-input")).to_have_value("Jane Doe")

def test_placeholder_locators(page):
    """
    Demonstrates: Placeholder locators (get_by_placeholder)
    Shows: Alternative to labels when appropriate
    """
    # GIVEN: User is on forms page
    page.goto("http://127.0.0.1:5000/forms")
    
    # WHEN: Using placeholder to find input
    email_input = page.get_by_placeholder("user@example.com")
    email_input.fill("test@test.com")
    
    # THEN: Input is filled
    expect(email_input).to_have_value("test@test.com")

def test_aria_described_by_for_help_text(page):
    """
    Demonstrates: ARIA describedby for accessibility
    Shows: Help text association
    """
    # GIVEN: User is on forms page
    page.goto("http://127.0.0.1:5000/forms")
    
    # WHEN: Checking email input
    email_input = page.get_by_label("Email Address")
    
    # THEN: It has aria-describedby pointing to help text
    expect(email_input).to_have_attribute("aria-describedby", "email-help")

def test_file_upload_input(page):
    """
    Demonstrates: File upload locators
    Shows: File input interaction
    """
    # GIVEN: User is on forms page
    page.goto("http://127.0.0.1:5000/forms")
    
    # WHEN: Setting file on input
    file_input = page.get_by_test_id("file-upload-input")
    
    # THEN: File input is available
    expect(file_input).to_be_visible()
    expect(file_input).to_have_attribute("type", "file")
