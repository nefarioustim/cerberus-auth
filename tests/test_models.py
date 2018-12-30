"""
Tests for models.
"""

import pytest

from cerberusauth import models as model_factories


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
    assert hasattr(model_obj, 'namespace')
    assert_object_matches_dict(model_obj, model_dict)


def test_user_model_requires_email_password_fullname(user):
    """."""
    with pytest.raises(TypeError) as exc:
        user()

    assert "email" in str(exc.value)


def test_user_model_instantiates(user, get_user):
    """."""
    assert_instantiation(user, get_user())


def test_user_model_new_password(user, get_user):
    """."""
    user_dict = get_user()
    user = user(**user_dict)

    assert user

    user.new_password(user_dict["password"])

    assert user.password != user_dict["password"]
    assert user.password.decode()


def test_user_model_authenticate(user, get_user):
    """."""
    user_dict = get_user()
    user = user(**user_dict)

    assert user

    user.new_password(user_dict["password"])

    assert user.authenticate(user_dict["password"])


@pytest.mark.parametrize("test_ns, expected_ns", [
    ("Wyrd Technology", "wyrd-technology"),
    ("___This is a test___", "this-is-a-test"),
    (None, None),
    (False, None)
])
def test_user_model_namespace(user, get_user, test_ns, expected_ns):
    """."""
    user = user(namespace=test_ns, **get_user())

    assert user
    assert user.namespace == expected_ns


def test_role_model_requires_name(role):
    """."""
    with pytest.raises(TypeError) as exc:
        role()

    assert "name" in str(exc.value)


def test_role_model_instantiates(role, get_role):
    """."""
    assert_instantiation(role, get_role())


@pytest.mark.parametrize("test_ns, expected_ns", [
    ("Wyrd Technology", "wyrd-technology"),
    ("___This is a test___", "this-is-a-test"),
    (None, None),
    (False, None)
])
def test_role_model_namespace(role, get_role, test_ns, expected_ns):
    """."""
    role = role(namespace=test_ns, **get_role())

    assert role
    assert role.namespace == expected_ns


def test_permission_model_requires_slug(permission):
    """."""
    with pytest.raises(TypeError) as exc:
        permission()

    assert "slug" in str(exc.value)


def test_permission_model_instantiates(permission, get_permission):
    """."""
    assert_instantiation(permission, get_permission())


@pytest.mark.parametrize("test_ns, expected_ns", [
    ("Wyrd Technology", "wyrd-technology"),
    ("___This is a test___", "this-is-a-test"),
    (None, None),
    (False, None)
])
def test_permission_model_namespace(
    permission, get_permission, test_ns, expected_ns
):
    """."""
    permission = permission(namespace=test_ns, **get_permission())

    assert permission
    assert permission.namespace == expected_ns


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
