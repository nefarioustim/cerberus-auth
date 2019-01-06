"""
Tests for models.
"""

from sqlalchemy.orm.base import object_mapper

from cerberusauth import models
from cerberusauth.models import sql

STORAGE_STRATEGY = 'sql'


def test_user_model_can_object_map_for_sql_alchemy(get_user):
    """."""
    user = models.user_factory(
        STORAGE_STRATEGY, **get_user()
    )
    # Raises exception if not ORM model.
    object_mapper(user)

    assert isinstance(user, sql.User)


def test_role_model_can_object_map_for_sql_alchemy(get_role):
    """."""
    role = models.role_factory(
        STORAGE_STRATEGY, **get_role()
    )
    # Raises exception if not ORM model.
    object_mapper(role)

    assert isinstance(role, sql.Role)


def test_permission_model_can_object_map_for_sql_alchemy(get_permission):
    """."""
    permission = models.permission_factory(
        STORAGE_STRATEGY, **get_permission()
    )
    # Raises exception if not ORM model.
    object_mapper(permission)

    assert isinstance(permission, sql.Permission)
