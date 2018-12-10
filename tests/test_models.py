"""
Tests for models.
"""

import pytest

from cerberusauth import models as model_factories

from .data_for_tests import get_user, get_role, get_permission


@pytest.fixture(params=[None, 'sql'])
def user(request):
    return model_factories.get_user_class(request.param)


@pytest.fixture(params=[None, 'sql'])
def role(request):
    return model_factories.get_role_class(request.param)


@pytest.fixture(params=[None, 'sql'])
def permission(request):
    return model_factories.get_permission_class(request.param)


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


def test_user_model_requires_email_password_fullname(user):
    """."""
    with pytest.raises(TypeError) as exc:
        user()

    assert "email" in str(exc.value)


def test_user_model_instantiates(user):
    """."""
    assert_instantiation(user, get_user())


def test_user_model_new_password(user):
    """."""
    user_dict = get_user()
    user = user(**user_dict)

    assert user

    user.new_password(user_dict["password"])

    assert user.password != user_dict["password"]
    assert user.password.decode()


def test_user_model_authenticate(user):
    """."""
    user_dict = get_user()
    user = user(**user_dict)

    assert user

    user.new_password(user_dict["password"])

    assert user.authenticate(user_dict["password"])


def test_role_model_requires_name(role):
    """."""
    with pytest.raises(TypeError) as exc:
        role()

    assert "name" in str(exc.value)


def test_role_model_instantiates(role):
    """."""
    assert_instantiation(role, get_role())


def test_permission_model_requires_slug(permission):
    """."""
    with pytest.raises(TypeError) as exc:
        permission()

    assert "slug" in str(exc.value)


def test_permission_model_instantiates(permission):
    """."""
    assert_instantiation(permission, get_permission())


@pytest.mark.parametrize("test_slug, expected_slug", [
    ("slug", "slug"),
    ("random-slug", "random-slug"),
    ("randomer/slug", "randomer-slug"),
    ("Something Else", "something-else"),
    ("___This is a test___", "this-is-a-test"),
    ("影師嗎", "ying-shi-ma"),
    ("C\'est déjà l\'été.", "c-est-deja-l-ete")
])
def test_permission_model_slugifys_slug(permission, test_slug, expected_slug):
    """."""
    permission = permission(slug=test_slug)

    assert permission
    assert permission.slug == expected_slug
