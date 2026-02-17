"""
i18n and localization tests
Demonstrates locale switching and localized UI/API-backed messaging.
"""
import re

import pytest
from playwright.sync_api import expect

BASE_URL = "http://127.0.0.1:5000"


@pytest.mark.i18n
def test_navigation_labels_localized_to_spanish(page):
    page.goto(f"{BASE_URL}/?lang=es")

    expect(page.get_by_test_id("nav-home")).to_have_text("Inicio")
    expect(page.get_by_test_id("nav-products")).to_have_text("Productos")
    expect(page.get_by_test_id("login-button")).to_have_text("Iniciar sesion")


@pytest.mark.i18n
def test_login_error_message_localized_to_spanish(page):
    page.goto(f"{BASE_URL}/login?lang=es")

    page.get_by_test_id("username-input").fill("invaliduser")
    page.get_by_test_id("password-input").fill("wrongpassword")
    page.get_by_test_id("submit-login-button").click()

    error_message = page.get_by_test_id("error-message")
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Usuario o contrasena invalido")


@pytest.mark.i18n
def test_locale_switcher_persists_across_pages(page):
    page.goto(f"{BASE_URL}/login")

    page.get_by_test_id("locale-es").click()

    expect(page).to_have_url(f"{BASE_URL}/login")
    expect(page.get_by_role("heading", name="Inicia sesion en tu cuenta")).to_be_visible()

    page.get_by_test_id("nav-products").click()
    expect(page).to_have_url(f"{BASE_URL}/products")
    expect(page.get_by_test_id("nav-home")).to_have_text("Inicio")


@pytest.mark.i18n
def test_login_error_message_defaults_to_english(page):
    page.goto(f"{BASE_URL}/login?lang=en")

    page.get_by_test_id("username-input").fill("invaliduser")
    page.get_by_test_id("password-input").fill("wrongpassword")
    page.get_by_test_id("submit-login-button").click()

    error_message = page.get_by_test_id("error-message")
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Invalid username or password")


@pytest.mark.i18n
def test_locale_aware_date_number_currency_for_english(page):
    page.goto(f"{BASE_URL}/?lang=en")

    expect(page.get_by_test_id("locale-demo-date")).to_have_text("02/16/2026")
    expect(page.get_by_test_id("locale-demo-number")).to_have_text("1,234,567.89")
    expect(page.get_by_test_id("locale-demo-currency")).to_have_text("$1,299.99")


@pytest.mark.i18n
def test_locale_aware_date_number_currency_for_spanish(page):
    page.goto(f"{BASE_URL}/?lang=es")

    expect(page.get_by_test_id("locale-demo-date")).to_have_text("16/02/2026")
    expect(page.get_by_test_id("locale-demo-number")).to_have_text("1.234.567,89")
    expect(page.get_by_test_id("locale-demo-currency")).to_have_text(re.compile(r"1\.299,99\s*€"))
