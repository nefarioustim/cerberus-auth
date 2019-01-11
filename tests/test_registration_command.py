"""
Tests for CommandRegisterUser.
"""

import pytest

from cerberusauth.registration import command
from cerberusauth import models


def test_create_register_users_command():
    """."""
    register_users = command.create_register_users_command()

    assert register_users
    assert isinstance(register_users, command.RegisterUsersCommand)
    assert callable(register_users)


@pytest.mark.parametrize("list_of_dicts, expected_count", [
    ([{"email": "joe.bloggs@somewhere.com", "id": "test"}], 1),
    ([
        {"email": "joe.bloggs@somewhere.com", "id": "test"},
        {"email": "joe.bloggs@somewhere.com", "id": "test"}
    ], 2),
    ([
        {"email": "joe.bloggs@somewhere.com", "id": "test", "foo": "bar"},
        {"email": "joe.bloggs@somewhere.com", "id": "test", "foo": "bar"}
    ], 2),
    ([
        {"email": "joe.bloggs@somewhere.com", "id": "test"},
        "GEOFF!"
    ], 1),
    ([
        {"email": "joe.bloggs@somewhere.com", "id": "test"},
        True
    ], 1),
    ([
        {"notemail": "joe.bloggs@somewhere.com", "id": "test"},
        {"email": "joe.bloggs@somewhere.com", "id": "test"},
    ], 1),
    ([
        "NO, JEFF!",
        {"id": "test", "fullname": "Joe Bloggs"},
        False
    ], 0)
])
def test_register_users_command(
    caplog, storage_session, list_of_dicts, expected_count
):
    """."""
    register_users = command.create_register_users_command(
        session=storage_session
    )

    with caplog.at_level("INFO"):
        users = register_users(*list_of_dicts)

    if expected_count > 0:
        assert users

    else:
        assert not users

    assert isinstance(users, list)
    assert len(users) == expected_count

    for registered_user in users:
        user = registered_user.user
        assert isinstance(user, models.BaseUser)
        assert user.password
        assert isinstance(user.password, bytes)
        assert user.password.decode()
        assert len(user.password) > 30

        temp_password = registered_user.temp_password
        assert isinstance(temp_password, str)
        assert len(temp_password) > 30

    assert 'Registered {} new User(s): {}'.format(
        expected_count,
        ', '.join([u.email for (u, p) in users])) in caplog.text
