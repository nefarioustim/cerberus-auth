"""
Tests for authentication module.
"""

from cerberusauth import authentication


def test_get_password():
    """."""
    password = authentication.get_password()

    assert password
    assert isinstance(password, str)
    assert len(password) > 29
