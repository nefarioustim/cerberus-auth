"""
Tests for RegisterService.
"""

from cerberusauth import register
from cerberusauth.register import command


def test_create_register_service():
    """."""
    reg = register.create_register_service()

    assert reg
    assert isinstance(reg, register.RegisterService)
    assert isinstance(reg.register_users, command.RegisterUsersCommand)
