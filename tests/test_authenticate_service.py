"""
Tests for AuthenticateService.
"""

from cerberusauth import authenticate


def test_get_password():
    """."""
    password = authenticate.AuthenticateService.get_password()

    assert password
    assert isinstance(password, str)
    assert len(password) > 29


def test_create_authenticate_service():
    """."""
    auth = authenticate.create_authenticate_service()

    assert auth
    assert isinstance(auth, authenticate.AuthenticateService)
