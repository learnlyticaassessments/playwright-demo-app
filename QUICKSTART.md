# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install Python Dependencies
```bash
pip install flask pytest pytest-playwright playwright
```

### Step 2: Install Playwright Browsers
```bash
playwright install
```

### Step 3: Start the Application
Open Terminal 1:
```bash
python app.py
```

Application will be running at: http://localhost:5000

### Step 4: Run Tests
Open Terminal 2:
```bash
# Run all tests
pytest tests/

# Run specific category
pytest tests/specs/auth/
pytest tests/specs/products/
pytest tests/specs/forms/
pytest tests/specs/components/

# Run single test
pytest tests/specs/auth/test_authentication.py::test_successful_login_with_test_ids -v
```

## 🎯 What to Explore

### In the Application (Browser)
1. Open http://localhost:5000
2. Try logging in (testuser / password123)
3. Explore products, forms, and components pages
4. See how UI elements are structured with test IDs and ARIA roles

### In the Code
1. **Locators** → `tests/locators/app_locators.py`
2. **Pages** → `tests/pages/app_pages.py`
3. **Components** → `tests/components/common_components.py`
4. **Tests** → `tests/specs/*/`

## 📚 Key Files to Study

### For Beginners
1. `tests/specs/auth/test_authentication.py` - Start here!
2. `tests/pages/app_pages.py` - See how pages work
3. `tests/locators/app_locators.py` - Understand locator contracts

### For Advanced
1. `tests/fixtures/base_fixtures.py` - Dependency injection
2. `tests/components/common_components.py` - Reusable components
3. `tests/specs/components/test_components.py` - Complex UI patterns

## 🧪 Test Credentials

| User Type | Username | Password |
|-----------|----------|----------|
| Regular   | testuser | password123 |
| Admin     | admin    | admin123 |

## 💡 Pro Tips

### Slow Down Tests for Demo
Edit `tests/fixtures/base_fixtures.py`:
```python
browser = p.chromium.launch(headless=False, slow_mo=1000)
```

### Run Tests Headless (Faster)
```python
browser = p.chromium.launch(headless=True)
```

### Debug a Failing Test
```bash
pytest tests/specs/auth/test_authentication.py::test_name -v --pdb
```

## 🎓 Learning Path

### Day 1: Basics
- Run the application
- Explore the UI
- Run authentication tests
- Read test code

### Day 2: Architecture
- Study Page Object Model
- Understand Component Layer
- Learn Locator Contracts
- Review Fixtures

### Day 3: Advanced
- Forms handling
- Dynamic content
- Complex components
- Multi-step flows

## ❓ Troubleshooting

### Port 5000 Already in Use
```bash
# Change port in app.py:
app.run(debug=True, port=5001)

# Update tests to use new port in page objects
```

### Tests Timing Out
- Increase timeout in fixtures
- Check if application is running
- Verify network connectivity

### Browser Not Opening
```bash
# Reinstall browsers
playwright install --force
```

## 📦 Directory Quick Reference

```
tests/
├── locators/          # What to find
├── pages/             # How to interact
├── components/        # Reusable pieces
├── fixtures/          # Test setup
└── specs/             # Actual tests
```

## 🎉 Next Steps

1. ✅ Run all tests successfully
2. ✅ Modify a locator and see impact
3. ✅ Add a new test case
4. ✅ Create a new page object
5. ✅ Extend a component

Happy Testing! 🚀
