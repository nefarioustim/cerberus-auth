"""
Tests for AuthoriseService commands.
"""

import pytest

from cerberusauth.authorise import command


def test_create_new_permissions_command():
    """."""
    new_permissions = command.create_new_permissions_command()

    assert new_permissions
    assert isinstance(new_permissions, command.NewPermissionsCommand)
    assert callable(new_permissions)


@pytest.mark.parametrize("list_of_dicts, expected_count", [
    ([{"slug": "Can Make Cheese"}], 1),
    ([
        {"slug": "Can Make Cheese"},
        True
    ], 1),
    ([
        "NO, JEFF!",
        {"id": "test", "fullname": "Joe Bloggs"},
        False
    ], 0)
])
def test_new_permissions_command(
    caplog, storage_session, list_of_dicts, expected_count
):
    """."""
    new_permissions = command.create_new_permissions_command(
        session=storage_session
    )

    with caplog.at_level("INFO"):
        permissions = new_permissions(*list_of_dicts)

    assert isinstance(permissions, list)
    assert len(permissions) == expected_count


def test_create_new_roles_command():
    """."""
    new_roles = command.create_new_roles_command()

    assert new_roles
    assert isinstance(new_roles, command.NewRolesCommand)
    assert callable(new_roles)


@pytest.mark.parametrize("list_of_dicts, expected_count", [
    ([{"name": "Admin"}], 1),
    ([
        {"name": "Admin"},
        True
    ], 1),
    ([
        "NO, JEFF!",
        {"id": "test", "fullname": "Joe Bloggs"},
        False
    ], 0)
])
def test_new_roles_command(
    caplog, storage_session, list_of_dicts, expected_count
):
    """."""
    new_roles = command.create_new_roles_command(
        session=storage_session
    )

    with caplog.at_level("INFO"):
        roles = new_roles(*list_of_dicts)

    assert isinstance(roles, list)
    assert len(roles) == expected_count
