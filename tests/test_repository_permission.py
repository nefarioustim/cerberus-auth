"""Tests for PermissionRepository."""

from unittest import mock

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
    repo.adapter.get = mock.Mock()

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
    repo.adapter.get = mock.Mock()

    with caplog.at_level("INFO"):
        repo.get(*test_ids)

    for test_id in test_ids:
        repo.adapter.get.assert_any_call(repo.agg_root_class, test_id)
        assert 'Got {} with ID {}'.format(
            repo.agg_root_class.__name__, test_id
        ) in caplog.text


def test_save(caplog):
    """."""
    repo = permission.get_repository()
    return_perm = repo.get_aggregate_root_object(
        data_for_tests.get_permission())
    return_perm.id = 1
    repo.adapter.save = mock.MagicMock(return_value=return_perm)
    repo.adapter.save.__name__ = 'save'

    with caplog.at_level("INFO"):
        repo.save(data_for_tests.get_permission())

    repo.adapter.save.assert_called_once()
    assert '{} {} with ID 1'.format(
        repo.adapter.save.__name__,
        repo.agg_root_class.__name__
    ) in caplog.text


def test_save_batch():
    """."""
    count = 5
    repo = permission.get_repository()
    repo.adapter.save = mock. Mock()
    list_of_dicts = [
        data_for_tests.get_permission(id='test') for i in range(count)
    ]

    saved = repo.save(*list_of_dicts)

    assert saved
    assert isinstance(saved, list)
    assert len(saved) == count


def test_delete(caplog):
    """."""
    repo = permission.get_repository()
    repo.adapter.delete = mock.MagicMock(return_value=None)
    repo.adapter.delete.__name__ = 'delete'

    with caplog.at_level("INFO"):
        repo.delete(data_for_tests.get_permission(id=1))

    repo.adapter.delete.assert_called_once()
    assert '{} {} with ID 1'.format(
        repo.adapter.delete.__name__,
        repo.agg_root_class.__name__
    ) in caplog.text


def test_delete_batch(caplog):
    """."""
    count = 5
    repo = permission.get_repository()
    repo.adapter.delete = mock.MagicMock(return_value=None)
    repo.adapter.delete.__name__ = 'delete'
    list_of_dicts = [
        data_for_tests.get_permission(id='test') for i in range(count)
    ]

    with caplog.at_level("INFO"):
        deleted = repo.delete(*list_of_dicts)

    assert deleted
    assert isinstance(deleted, list)
    assert len(deleted) == count
    assert len(caplog.records) == count
    assert '{} {} with ID test'.format(
        repo.adapter.delete.__name__,
        repo.agg_root_class.__name__
    ) in caplog.text
