"""
Simple i18n helpers for localization demos.
"""
from datetime import date, datetime

DEFAULT_LOCALE = "en"
SUPPORTED_LOCALES = ("en", "es")

TRANSLATIONS = {
    "en": {
        "app.title": "Playwright Demo Store",
        "nav.home": "Home",
        "nav.products": "Products",
        "nav.forms": "Forms Demo",
        "nav.components": "Components",
        "nav.cart": "Cart",
        "nav.login": "Login",
        "nav.language": "Language",
        "footer.privacy": "Privacy Policy",
        "footer.terms": "Terms of Service",
        "footer.contact": "Contact Us",
        "auth.login_title": "Login to Your Account",
        "auth.register_title": "Create Your Account",
        "auth.username": "Username",
        "auth.password": "Password",
        "auth.email": "Email",
        "auth.confirm_password": "Confirm Password",
        "auth.remember_me": "Remember me",
        "auth.sign_in": "Sign In",
        "auth.create_account": "Create Account",
        "auth.no_account": "Don't have an account?",
        "auth.register_here": "Register here",
        "auth.already_account": "Already have an account?",
        "auth.login_here": "Login here",
        "auth.forgot_password": "Forgot password?",
        "auth.terms_accept": "I agree to the Terms and Conditions",
        "auth.test_credentials": "Test Credentials",
        "errors.generic": "An error occurred. Please try again.",
        "errors.password_mismatch": "Passwords do not match",
        "errors.accept_terms": "Please accept the terms and conditions",
        "api.login.success": "Login successful",
        "api.login.invalid": "Invalid username or password",
        "api.register.user_exists": "Username already exists",
        "api.register.success": "Registration successful",
        "api.order.login_required": "Please login",
        "api.order.success": "Order placed successfully",
        "api.profile.unauthorized": "Unauthorized",
        "api.profile.updated": "Profile updated successfully",
        "api.product.not_found": "Product not found",
        "i18n.demo_title": "Locale Formatting Demo",
        "i18n.demo_date": "Date",
        "i18n.demo_number": "Number",
        "i18n.demo_currency": "Currency",
    },
    "es": {
        "app.title": "Tienda Demo Playwright",
        "nav.home": "Inicio",
        "nav.products": "Productos",
        "nav.forms": "Demo Formularios",
        "nav.components": "Componentes",
        "nav.cart": "Carrito",
        "nav.login": "Iniciar sesion",
        "nav.language": "Idioma",
        "footer.privacy": "Politica de Privacidad",
        "footer.terms": "Terminos de Servicio",
        "footer.contact": "Contactanos",
        "auth.login_title": "Inicia sesion en tu cuenta",
        "auth.register_title": "Crea tu cuenta",
        "auth.username": "Usuario",
        "auth.password": "Contrasena",
        "auth.email": "Correo",
        "auth.confirm_password": "Confirmar Contrasena",
        "auth.remember_me": "Recordarme",
        "auth.sign_in": "Entrar",
        "auth.create_account": "Crear cuenta",
        "auth.no_account": "No tienes cuenta?",
        "auth.register_here": "Registrate aqui",
        "auth.already_account": "Ya tienes cuenta?",
        "auth.login_here": "Inicia sesion aqui",
        "auth.forgot_password": "Olvidaste tu contrasena?",
        "auth.terms_accept": "Acepto los Terminos y Condiciones",
        "auth.test_credentials": "Credenciales de prueba",
        "errors.generic": "Ocurrio un error. Intenta nuevamente.",
        "errors.password_mismatch": "Las contrasenas no coinciden",
        "errors.accept_terms": "Acepta los terminos y condiciones",
        "api.login.success": "Inicio de sesion exitoso",
        "api.login.invalid": "Usuario o contrasena invalido",
        "api.register.user_exists": "El usuario ya existe",
        "api.register.success": "Registro exitoso",
        "api.order.login_required": "Por favor inicia sesion",
        "api.order.success": "Pedido realizado con exito",
        "api.profile.unauthorized": "No autorizado",
        "api.profile.updated": "Perfil actualizado con exito",
        "api.product.not_found": "Producto no encontrado",
        "i18n.demo_title": "Demo de Formato por Idioma",
        "i18n.demo_date": "Fecha",
        "i18n.demo_number": "Numero",
        "i18n.demo_currency": "Moneda",
    },
}


def normalize_locale(locale: str | None) -> str:
    if not locale:
        return DEFAULT_LOCALE
    normalized = locale.lower().strip().split("-")[0]
    if normalized in SUPPORTED_LOCALES:
        return normalized
    return DEFAULT_LOCALE


def detect_locale_from_header(accept_language: str | None) -> str:
    if not accept_language:
        return DEFAULT_LOCALE
    first = accept_language.split(",")[0].strip()
    return normalize_locale(first)


def translate(key: str, locale: str, **kwargs) -> str:
    safe_locale = normalize_locale(locale)
    value = TRANSLATIONS.get(safe_locale, {}).get(key)
    if value is None:
        value = TRANSLATIONS[DEFAULT_LOCALE].get(key, key)
    if kwargs:
        return value.format(**kwargs)
    return value


def _locale_format_config(locale: str) -> dict[str, str]:
    safe_locale = normalize_locale(locale)
    if safe_locale == "es":
        return {
            "decimal_sep": ",",
            "thousand_sep": ".",
            "date_format": "dd/mm/yyyy",
            "currency_symbol": "€",
            "currency_suffix": " €",
        }
    return {
        "decimal_sep": ".",
        "thousand_sep": ",",
        "date_format": "mm/dd/yyyy",
        "currency_symbol": "$",
        "currency_suffix": "",
    }


def format_number(value: float, locale: str, decimals: int = 2) -> str:
    cfg = _locale_format_config(locale)
    base = f"{value:,.{decimals}f}"
    if cfg["decimal_sep"] == "." and cfg["thousand_sep"] == ",":
        return base
    transformed = base.replace(",", "_").replace(".", cfg["decimal_sep"]).replace("_", cfg["thousand_sep"])
    return transformed


def format_currency(value: float, locale: str) -> str:
    safe_locale = normalize_locale(locale)
    if safe_locale == "es":
        return f"{format_number(value, safe_locale)}{_locale_format_config(safe_locale)['currency_suffix']}"
    return f"{_locale_format_config(safe_locale)['currency_symbol']}{format_number(value, safe_locale)}"


def format_date(value: date | datetime, locale: str) -> str:
    cfg = _locale_format_config(locale)
    if isinstance(value, datetime):
        value = value.date()
    if cfg["date_format"] == "dd/mm/yyyy":
        return value.strftime("%d/%m/%Y")
    return value.strftime("%m/%d/%Y")
