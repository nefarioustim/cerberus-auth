"""Tests for PermissionRepository."""

from unittest import mock

import pytest

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


def test_count_calls_adapter():
    """."""
    repo = permission.get_repository()
    repo.adapter = mock.Mock()

    repo.count()

    repo.adapter.count.assert_called_once()
    repo.adapter.count.assert_called_with(repo.agg_root_class)


def test_get(caplog):
    """."""
    repo = permission.get_repository()
    repo.adapter = mock.Mock()

    with caplog.at_level("INFO"):
        repo.get(1)

    repo.adapter.get.assert_called_once_with(repo.agg_root_class, 1)
    assert 'Got {} with ID 1'.format(
        repo.agg_root_class.__name__
    ) in caplog.text


def test_get_batch(caplog):
    """."""
    test_ids = [1, 2, 3, 4]
    repo = permission.get_repository()
    repo.adapter = mock.Mock()

    with caplog.at_level("INFO"):
        repo.get(*test_ids)

    for test_id in test_ids:
        repo.adapter.get.assert_any_call(repo.agg_root_class, test_id)
        assert 'Got {} with ID {}'.format(
            repo.agg_root_class.__name__, test_id
        ) in caplog.text
