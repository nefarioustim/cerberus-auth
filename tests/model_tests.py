"""
Tests for models.
"""

from datetime import datetime
import pytest

from .data_for_tests import get_user, get_role, get_permission


def assert_object_matches_dict(obj, dic):
    """Assert object properties match dict keys."""
    for (key, value) in dic.items():
        assert getattr(obj, key) == value


def assert_instantiation(model_cls, model_dict):
    """Assert the instantiation of a model class."""
    model_obj = model_cls(**model_dict)

    assert model_obj
    assert isinstance(model_obj, model_cls)
    assert model_obj.is_enabled is True
    assert model_obj.is_deleted is False
    assert model_obj.created is not None
    assert model_obj.modified == model_obj.created
    assert_object_matches_dict(model_obj, model_dict)


def test_user_model_requires_email_password_fullname(models):
    """."""
    with pytest.raises(TypeError) as exc:
        models.User()

    assert "email" in str(exc.value)


def test_user_model_instantiates(models):
    """."""
    assert_instantiation(models.User, get_user())


def test_user_model_new_password(models):
    """."""
    user_dict = get_user()
    user = models.User(**user_dict)

    assert user

    user.new_password(user_dict["password"])

    assert user.password != user_dict["password"]
    assert user.password.decode()


def test_user_model_authenticate(models):
    """."""
    user_dict = get_user()
    user = models.User(**user_dict)

    assert user

    user.new_password(user_dict["password"])

    assert user.authenticate(user_dict["password"])


def test_role_model_requires_name(models):
    """."""
    with pytest.raises(TypeError) as exc:
        models.Role()

    assert "name" in str(exc.value)


def test_role_model_instantiates(models):
    """."""
    assert_instantiation(models.Role, get_role())


def test_permission_model_requires_slug(models):
    """."""
    with pytest.raises(TypeError) as exc:
        models.Permission()

    assert "slug" in str(exc.value)


def test_permission_model_instantiates(models):
    """."""
    assert_instantiation(models.Permission, get_permission())


@pytest.mark.parametrize("test_slug, expected_slug", [
    ("slug", "slug"),
    ("random-slug", "random-slug"),
    ("randomer/slug", "randomer-slug"),
    ("Something Else", "something-else"),
    ("___This is a test___", "this-is-a-test"),
    ("影師嗎", "ying-shi-ma"),
    ("C\'est déjà l\'été.", "c-est-deja-l-ete")
])
def test_permission_model_slugifys_slug(models, test_slug, expected_slug):
    """."""
    permission = models.Permission(slug=test_slug)

    assert permission
    assert permission.slug == expected_slug
