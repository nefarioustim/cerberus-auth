"""
Tests for models.
"""

import pytest

from cerberusauth import models

from .data_for_tests import get_user, get_role, get_permission


def test_user_model_requires_email_password_fullname():
    """."""
    with pytest.raises(TypeError) as exc:
        models.User()

    assert "email" in str(exc.value)
    assert "password" in str(exc.value)
    assert "fullname" in str(exc.value)


def test_user_model_instantiates():
    """."""
    user = models.User(**get_user())

    assert user
    assert isinstance(user, models.User)


def test_role_model_requires_name():
    """."""
    with pytest.raises(TypeError) as exc:
        models.Role()

    assert "name" in str(exc.value)


def test_role_model_instantiates():
    """."""
    role = models.Role(**get_role())

    assert role
    assert isinstance(role, models.Role)


def test_permission_model_requires_slug():
    """."""
    with pytest.raises(TypeError) as exc:
        models.Permission()

    assert "slug" in str(exc.value)


def test_permission_model_instantiates():
    """."""
    permission = models.Permission(**get_permission())

    assert permission
    assert isinstance(permission, models.Permission)
