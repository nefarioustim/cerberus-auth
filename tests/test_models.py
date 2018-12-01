"""
Tests for models.
"""

from datetime import datetime
import bcrypt
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
    user_dict = get_user()
    user = models.User(**user_dict)

    assert user
    assert isinstance(user, models.User)
    assert user.password != user_dict['password']
    assert user.created is not None
    assert isinstance(user.created, datetime)
    assert user.modified == user.created

    user.id = 1

    assert user.modified > user.created


def test_user_model_authenticate():
    """."""
    user_dict = get_user()
    user = models.User(**user_dict)

    assert user
    assert user.authenticate(user_dict["password"])


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
    assert role.created is not None
    assert isinstance(role.created, datetime)
    assert role.modified == role.created

    role.id = 1

    assert role.modified > role.created


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
    assert permission.created is not None
    assert isinstance(permission.created, datetime)
    assert permission.modified == permission.created

    permission.id = 1

    assert permission.modified > permission.created


@pytest.mark.parametrize("test_slug, expected_slug", [
    ('slug', 'slug'),
    ('random-slug', 'random-slug'),
    ('randomer/slug', 'randomer-slug'),
    ('Something Else', 'something-else'),
    ('___This is a test___', 'this-is-a-test'),
    ('影師嗎', 'ying-shi-ma'),
    ('C\'est déjà l\'été.', 'c-est-deja-l-ete')
])
def test_permission_model_slugifys_slug(test_slug, expected_slug):
    """."""
    permission = models.Permission(slug=test_slug)

    assert permission
    assert permission.slug == expected_slug
