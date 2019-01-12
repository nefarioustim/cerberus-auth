"""
Tests for AuthoriseService commands.
"""

from cerberusauth.authorise import command


def test_create_new_permissions_command():
    """."""
    new_permissions = command.create_new_permissions_command()

    assert new_permissions
    assert isinstance(new_permissions, command.NewPermissionsCommand)
    assert callable(new_permissions)
