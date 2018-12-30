"""
Tests for RegistrationService.
"""

from cerberusauth import registration
from cerberusauth.registration import command


def test_create_registration_service():
    """."""
    reg = registration.create_registration_service()

    assert reg
    assert isinstance(reg, registration.RegistrationService)
    assert isinstance(reg.register_users, command.RegisterUsersCommand)
