"""Tests for PermissionRepository."""

from cerberusauth.repository import permission
from cerberusauth.repository.adapter import sql
from cerberusauth.models import sql as sql_models

from . import data_for_tests


def test_permission_repository_factory():
    """."""
    repo = permission.get_repository()

    assert repo
    assert isinstance(repo, permission.PermissionRepository)
    assert isinstance(repo.adapter, sql.SQLRepositoryAdapter)
    assert repo.agg_root_class is sql_models.Permission


def test_get_aggregate_root_object_returns_permission():
    """."""
    repo = permission.get_repository()

    agg_root = repo.get_aggregate_root_object(
        data_for_tests.get_permission()
    )

    assert agg_root
    assert isinstance(agg_root, repo.agg_root_class)

    # Assert sending it an aggregate root object also works.
    agg_root = repo.get_aggregate_root_object(agg_root)

    assert agg_root
    assert isinstance(agg_root, repo.agg_root_class)
