"""
Tests for models.
"""

from sqlalchemy.orm.base import object_mapper

from cerberusauth import models

from .data_for_tests import get_user, get_role, get_permission

STORAGE_STRATEGY = 'sql'


def test_user_model_can_object_map_for_sql_alchemy():
    """."""
    # Raises exception if not ORM model.
    object_mapper(
        models.user_factory(STORAGE_STRATEGY, **get_user())
    )


def test_role_model_can_object_map_for_sql_alchemy():
    """."""
    # Raises exception if not ORM model.
    object_mapper(
        models.role_factory(STORAGE_STRATEGY, **get_role())
    )


def test_permission_model_can_object_map_for_sql_alchemy():
    """."""
    # Raises exception if not ORM model.
    object_mapper(
        models.permission_factory(STORAGE_STRATEGY, **get_permission())
    )
