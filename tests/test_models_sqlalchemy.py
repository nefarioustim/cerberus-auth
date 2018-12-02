"""
Tests for SQLAlchemy models.
"""

import pytest

from sqlalchemy.orm.base import object_mapper

from cerberusauth.models import sqlalchemy as sqlalchemy_models

from .data_for_tests import get_user, get_role, get_permission
from .model_tests import *


@pytest.fixture
def models():
    """Models fixture."""
    return sqlalchemy_models


def test_user_model_can_object_map_for_sql_alchemy(models):
    """."""
    # Raises exception if not ORM model.
    object_mapper(models.User(**get_user()))


def test_role_model_can_object_map_for_sql_alchemy(models):
    """."""
    # Raises exception if not ORM model.
    object_mapper(models.Role(**get_role()))


def test_permission_model_can_object_map_for_sql_alchemy(models):
    """."""
    # Raises exception if not ORM model.
    object_mapper(models.Permission(**get_permission()))
