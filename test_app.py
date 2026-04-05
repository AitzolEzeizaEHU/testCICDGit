"""Tests for app.py"""

from app import add, greet


def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_greet():
    """Test the greet function."""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("World") == "Hello, World!"


def test_add_with_negative_numbers():
    """Test add with negative numbers."""
    assert add(-5, -3) == -8
    assert add(-10, 5) == -5
