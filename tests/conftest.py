"""
conftest.py - Pytest configuration
Automatically loads fixtures for all tests
"""
pytest_plugins = [
    "tests.fixtures.base_fixtures",
]
