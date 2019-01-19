"""
Tests for AuthenticateService commands.
"""

from unittest.mock import Mock

import jwt
import pytest

from cerberusauth import config
from cerberusauth.authenticate import command
from cerberusauth.models import user_factory


def test_create_authenticate_user_command():
    """."""
    authenticate_user = command.create_authenticate_user_command()

    assert authenticate_user
    assert isinstance(authenticate_user, command.AuthenticateUserCommand)
    assert callable(authenticate_user)


def test_authenticate_user_command(caplog, storage_session):
    """."""
    authenticate_user = command.create_authenticate_user_command(
        session=storage_session
    )
    user = user_factory(email='something')
    user.set_password('my awesome password')
    authenticate_user.user_repository.get_by = Mock(return_value=[user])

    with caplog.at_level("INFO"):
        token = authenticate_user(
            email='something', password='my awesome password')

    assert token
    assert isinstance(token, bytes)

    token = jwt.decode(token, config.SECRET, algorithms=['HS256'])

    assert "id" in token and token["id"] is None
    assert "email" in token and token["email"] == "something"


def test_authenticate_user_command_bad_password(caplog, storage_session):
    """."""
    authenticate_user = command.create_authenticate_user_command(
        session=storage_session
    )
    user = user_factory(email='something')
    user.set_password('my awesome password')
    authenticate_user.user_repository.get_by = Mock(return_value=[user])

    with caplog.at_level("INFO"):
        token = authenticate_user(
            email='something', password='geoff1234')

    assert not token
    assert token is False


def test_authenticate_user_command_no_user(caplog, storage_session):
    """."""
    authenticate_user = command.create_authenticate_user_command(
        session=storage_session
    )
    authenticate_user.user_repository.get_by = Mock(return_value=[None])

    with caplog.at_level("INFO"):
        token = authenticate_user(
            email='geoff', password='my awesome password')

    assert not token
    assert token is False


def test_create_authenticate_token_command():
    """."""
    authenticate_token = command.create_authenticate_token_command()

    assert authenticate_token
    assert isinstance(authenticate_token, command.AuthenticateTokenCommand)
    assert callable(authenticate_token)


def test_authenticate_token_command(caplog, storage_session):
    """."""
    authenticate_token = command.create_authenticate_token_command()
    authenticate_user = command.create_authenticate_user_command(
        session=storage_session
    )
    user = user_factory(email='something')
    user.set_password('my awesome password')
    authenticate_user.user_repository.get_by = Mock(return_value=[user])
    token = authenticate_user(
        email='something', password='my awesome password')

    with caplog.at_level("INFO"):
        returned_token = authenticate_token(token)

    assert returned_token
    assert isinstance(returned_token, dict)
    assert "id" in returned_token and returned_token["id"] is None
    assert "email" in returned_token and returned_token["email"] == "something"


@pytest.mark.parametrize("bad_token", [
    (b"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6bnVsbCwiZW1haWwiOiJzb21"
     b"ldGhpbmciLCJleHAiOjE1NDc5MzAwMzd9.0PQSV6LcQPhffZzavgRrCXMvFzRiSZJl_L"
     b"pkpnGuIyr",),
    (None,),
    (False,),
    ("Geoff",),
    ("",)
])
def test_authenticate_token_command_failure(
    caplog, storage_session, bad_token
):
    """."""
    authenticate_token = command.create_authenticate_token_command()

    with caplog.at_level("INFO"):
        returned_token = authenticate_token(bad_token)

    assert not returned_token
    assert returned_token is False
