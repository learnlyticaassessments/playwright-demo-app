# Playwright Demo Application - Complete Locator Strategy Showcase

A comprehensive web application demonstrating all Playwright locator strategies, best practices, and enterprise-grade test automation architecture.

## 🎯 Purpose

This application is designed to showcase:
- ✅ All locator strategies from the Playwright Locator Strategy Guide (35-page document)
- ✅ Enterprise-grade test automation architecture
- ✅ Page Object Model (POM) pattern
- ✅ Component Object Model pattern
- ✅ Locator Contract Layer
- ✅ Dependency Injection with fixtures
- ✅ Real-world UI patterns (modals, tabs, forms, tables, etc.)

## 📁 Project Structure

```
playwright-demo-app/
│
├── app.py                          # Flask application
├── requirements.txt                # Python dependencies
│
├── templates/                      # HTML templates
│   ├── base.html                   # Base template with navigation
│   ├── home.html                   # Home page
│   ├── login.html                  # Login page
│   ├── register.html               # Registration page
│   ├── products.html               # Products listing
│   ├── checkout.html               # Checkout page
│   ├── dashboard.html              # User dashboard
│   ├── forms_demo.html             # Forms demonstration
│   └── components_demo.html        # UI components demo
│
├── static/
│   ├── css/
│   │   └── style.css               # Application styles
│   └── js/
│       └── main.js                 # JavaScript utilities
│
└── tests/                          # Playwright tests
    ├── conftest.py                 # Pytest configuration
    │
    ├── locators/                   # Locator Contract Layer
    │   └── app_locators.py         # Centralized locator definitions
    │
    ├── components/                 # Reusable Components
    │   └── common_components.py    # Navigation, Modal, Alert components
    │
    ├── pages/                      # Page Object Model
    │   └── app_pages.py            # Page classes with business APIs
    │
    ├── fixtures/                   # Dependency Injection
    │   └── base_fixtures.py        # Pytest fixtures for DI
    │
    └── specs/                      # Test Specifications
        ├── auth/
        │   └── test_authentication.py      # Login/Register tests
        ├── products/
        │   └── test_products.py            # Products tests
        ├── forms/
        │   └── test_forms.py               # Forms tests
        └── components/
            └── test_components.py          # UI components tests
```

## 🚀 Setup Instructions

### Prerequisites

- Python 3.8+
- pip

### Step 1: Install Dependencies

```bash
cd playwright-demo-app
pip install -r requirements.txt
```

### Step 2: Install Playwright Browsers

```bash
playwright install
```

### Step 3: Start the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Step 4: Run Tests (in a new terminal)

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/specs/auth/test_authentication.py

# Run with verbose output
pytest tests/ -v

# Run specific test
pytest tests/specs/auth/test_authentication.py::test_successful_login_with_test_ids
```

## 🎓 Locator Strategies Demonstrated

### 1. Test ID Locators (Priority: Low - Reliable fallback)
```python
page.get_by_test_id("login-button")
page.get_by_test_id("username-input")
```
**Use when:** Element lacks semantic attributes but needs stable identification

### 2. Role-Based Locators (Priority: HIGHEST - Most resilient)
```python
page.get_by_role("button", name="Submit")
page.get_by_role("checkbox", name="Accept terms")
page.get_by_role("textbox", name="Email")
```
**Use when:** Element has proper ARIA role (best practice)

### 3. Label Locators (Priority: High - Excellent for forms)
```python
page.get_by_label("Username")
page.get_by_label("Password")
```
**Use when:** Form inputs with associated labels

### 4. Text Locators (Priority: Medium - Good for unique text)
```python
page.get_by_text("Welcome")
page.get_by_text(re.compile(r"submit", re.IGNORECASE))
```
**Use when:** Element has unique, stable text content

### 5. Placeholder Locators (Priority: Medium)
```python
page.get_by_placeholder("Enter email")
```
**Use when:** Input has unique placeholder text

### 6. CSS Selectors (Priority: Lowest - Last resort)
```python
page.locator("div.modal > button.primary")
```
**Use when:** No semantic locator available

## 📚 Architecture Patterns

### Locator Contract Layer
**Purpose:** Centralize all locator definitions in one place

```python
class LoginLocators:
    USERNAME_INPUT = "username-input"
    PASSWORD_INPUT = "password-input"
    SUBMIT_BUTTON = "submit-login-button"
```

**Benefit:** When UI changes, update locators in ONE place

### Page Object Model
**Purpose:** Expose business APIs, hide implementation

```python
class LoginPage:
    def login(self, username: str, password: str):
        self.page.get_by_test_id(LoginLocators.USERNAME_INPUT).fill(username)
        self.page.get_by_test_id(LoginLocators.PASSWORD_INPUT).fill(password)
        self.page.get_by_test_id(LoginLocators.SUBMIT_BUTTON).click()
```

**Benefit:** Tests remain clean and readable

### Component Object Model
**Purpose:** Reusable UI components

```python
class NavigationComponent:
    def navigate_to_products(self):
        self.page.get_by_test_id("nav-products").click()
```

**Benefit:** Reuse across multiple pages

### Dependency Injection with Fixtures
**Purpose:** Provide ready-to-use objects to tests

```python
@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

def test_login(login_page):  # Automatically injected
    login_page.login("user", "pass")
```

**Benefit:** No manual object creation in tests

## 🧪 Test Examples

### Clean Test Using Architecture
```python
def test_user_can_place_order(login_page, products_page, checkout_page):
    # GIVEN: User is logged in
    login_page.navigate()
    login_page.login("testuser", "password123")
    
    # WHEN: User adds product and checks out
    products_page.navigate()
    products_page.add_product_to_cart(1)
    
    checkout_page.navigate()
    checkout_page.complete_checkout("123 Main St", "New York")
    
    # THEN: Order is placed
    message = checkout_page.get_checkout_message()
    assert "Order placed successfully" in message
```

**Notice:**
- ❌ No CSS selectors
- ❌ No XPath
- ❌ No locators in test
- ✅ Only business intent

## 🎯 Test Credentials

The application includes test users:

**Regular User:**
- Username: `testuser`
- Password: `password123`

**Admin User:**
- Username: `admin`
- Password: `admin123`

## 📄 Application Features

### Home Page (`/`)
- Hero section
- Feature cards
- Categories
- Newsletter subscription

### Authentication
- Login (`/login`)
- Registration (`/register`)
- Dashboard (`/dashboard`)
- Profile (`/profile`)

### Products
- Product listing (`/products`)
- Category filtering
- Search functionality
- Add to cart
- Product details

### Forms Demo (`/forms`)
Demonstrates ALL form input types:
- Text inputs
- Email inputs
- Dropdowns (select)
- Radio buttons
- Checkboxes
- Date/time inputs
- Textarea
- File uploads
- Form validation
- Multi-step form

### Components Demo (`/components`)
Demonstrates ALL UI patterns:
- Modal dialogs
- Dropdown menus
- Tabs
- Alerts
- Accordion
- Data tables
- Progress bars
- Toast notifications

## 🔧 Configuration

### Running Tests Headless
```python
# In fixtures/base_fixtures.py, change:
browser = p.chromium.launch(headless=True)
```

### Slowing Down Tests for Demo
```python
# In fixtures/base_fixtures.py:
browser = p.chromium.launch(headless=False, slow_mo=1000)  # 1 second delay
```

## 📊 Test Coverage

This application covers:

✅ **Authentication flows**
✅ **Form validation**
✅ **Dynamic content loading**
✅ **Filtering and search**
✅ **Multi-step processes**
✅ **Modal interactions**
✅ **Tab navigation**
✅ **Table operations**
✅ **Alert handling**
✅ **Role-based access**
✅ **State management**

## 🏆 Best Practices Demonstrated

1. **Locator Priority Hierarchy** - Always prefer role > label > test ID > CSS
2. **Strictness Handling** - Properly handle multi-element matches
3. **Auto-waiting** - Leverage Playwright's built-in waits
4. **Page Object Model** - Encapsulate page logic
5. **Component Reusability** - Share common components
6. **Centralized Locators** - Single source of truth
7. **Dependency Injection** - Clean test setup
8. **Accessibility First** - Use ARIA roles and labels

## 🚫 Anti-Patterns to Avoid

❌ **Locators in test files**
❌ **Deep CSS chains**
❌ **nth-child selectors**
❌ **time.sleep() delays**
❌ **Magic strings**
❌ **Ignoring strictness errors with first()**

## 📖 Learning Path

1. **Start with:** `tests/specs/auth/test_authentication.py`
   - Learn basic locator strategies
   
2. **Move to:** `tests/specs/products/test_products.py`
   - Learn dynamic content handling
   
3. **Then:** `tests/specs/forms/test_forms.py`
   - Master all input types
   
4. **Finally:** `tests/specs/components/test_components.py`
   - Complex UI patterns

## 🤝 Contributing

This is a demonstration project. Feel free to:
- Add more test scenarios
- Improve page objects
- Add new components
- Enhance documentation

## 📝 License

This project is for educational purposes.

## 🎉 Conclusion

This application demonstrates professional, enterprise-grade Playwright test automation. The architecture ensures:

- **Maintainability:** Locator changes in one place
- **Scalability:** Easy to add new pages/tests
- **Readability:** Tests read like business requirements
- **Reliability:** Uses best locator practices
- **Reusability:** Components used across tests

**Perfect for:** Interviews, portfolio, learning, team training, proof of concept

---

**Created to showcase the complete Playwright Locator Strategy Guide**
