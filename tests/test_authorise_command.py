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
