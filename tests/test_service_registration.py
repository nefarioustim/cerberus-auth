"""
Tests for RegistrationService.
"""

from cerberusauth import registration


def test_create_registration_service():
    """."""
    reg = registration.create_registration_service()

    assert reg
    assert isinstance(reg, registration.RegistrationService)
