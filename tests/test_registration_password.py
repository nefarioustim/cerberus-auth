"""
Tests for registration password creation.
"""

from cerberusauth.registration import password as pw


def test_get_password():
    """."""
    password = pw.get_password()

    assert password
    assert isinstance(password, str)
    assert len(password) > 29
