"""Tests for PermissionRepository."""

from unittest import mock

import pytest

from cerberusauth.repository import permission, role, user
from cerberusauth.repository.adapter import sql
from cerberusauth.models import sql as sql_models

from . import data_for_tests


@pytest.fixture(params=[{
    'factory': permission.get_repository,
    'repo_class': permission.PermissionRepository,
    'repo_adapter_class': sql.SQLRepositoryAdapter,
    'model_class': sql_models.Permission,
    'data_factory': data_for_tests.get_permission
}, {
    'factory': role.get_repository,
    'repo_class': role.RoleRepository,
    'repo_adapter_class': sql.SQLRepositoryAdapter,
    'model_class': sql_models.Role,
    'data_factory': data_for_tests.get_role
}, {
    'factory': user.get_repository,
    'repo_class': user.UserRepository,
    'repo_adapter_class': sql.SQLRepositoryAdapter,
    'model_class': sql_models.User,
    'data_factory': data_for_tests.get_user
}], ids=["permission", "role", "user"])
def repo_fixture(request):
    """Fixture for repo tests."""
    return request.param


def test_repository_factory(repo_fixture):
    """."""
    repo = repo_fixture['factory']()

    assert repo
    assert isinstance(repo, repo_fixture['repo_class'])
    assert isinstance(repo.adapter, repo_fixture['repo_adapter_class'])
    assert repo.agg_root_class is repo_fixture['model_class']


def test_get_aggregate_root_object_returns_correct_agg_root(repo_fixture):
    """."""
    repo = repo_fixture['factory']()

    agg_root = repo.get_aggregate_root_object(
        repo_fixture['data_factory']()
    )

    assert agg_root
    assert isinstance(agg_root, repo.agg_root_class)

    # Assert sending it an aggregate root object also works.
    agg_root = repo.get_aggregate_root_object(agg_root)

    assert agg_root
    assert isinstance(agg_root, repo.agg_root_class)


def test_count_calls_adapter(repo_fixture):
    """."""
    repo = repo_fixture['factory']()
    repo.adapter = mock.Mock()

    repo.count()

    repo.adapter.count.assert_called_once()
    repo.adapter.count.assert_called_with(repo.agg_root_class)


def test_get(caplog, repo_fixture):
    """."""
    repo = repo_fixture['factory']()
    repo.adapter.get = mock.Mock()

    with caplog.at_level("INFO"):
        repo.get(1)

    repo.adapter.get.assert_called_once_with(repo.agg_root_class, 1)
    assert 'Got {} with ID 1'.format(
        repo.agg_root_class.__name__
    ) in caplog.text


def test_get_batch(caplog, repo_fixture):
    """."""
    test_ids = [1, 2, 3, 4]
    repo = repo_fixture['factory']()
    repo.adapter.get = mock.Mock()

    with caplog.at_level("INFO"):
        repo.get(*test_ids)

    for test_id in test_ids:
        repo.adapter.get.assert_any_call(repo.agg_root_class, test_id)
        assert 'Got {} with ID {}'.format(
            repo.agg_root_class.__name__, test_id
        ) in caplog.text


def test_save(caplog, repo_fixture):
    """."""
    repo = repo_fixture['factory']()
    return_perm = repo.get_aggregate_root_object(
        repo_fixture['data_factory']())
    return_perm.id = 1
    repo.adapter.save = mock.MagicMock(return_value=return_perm)
    repo.adapter.save.__name__ = 'save'

    with caplog.at_level("INFO"):
        repo.save(repo_fixture['data_factory']())

    repo.adapter.save.assert_called_once()
    assert '{} {} with ID 1'.format(
        repo.adapter.save.__name__,
        repo.agg_root_class.__name__
    ) in caplog.text


def test_save_batch(repo_fixture):
    """."""
    count = 5
    repo = repo_fixture['factory']()
    repo.adapter.save = mock. Mock()
    list_of_dicts = [
        repo_fixture['data_factory'](id='test') for i in range(count)
    ]

    saved = repo.save(*list_of_dicts)

    assert saved
    assert isinstance(saved, list)
    assert len(saved) == count


def test_delete(caplog, repo_fixture):
    """."""
    repo = repo_fixture['factory']()
    repo.adapter.delete = mock.MagicMock(return_value=None)
    repo.adapter.delete.__name__ = 'delete'

    with caplog.at_level("INFO"):
        repo.delete(repo_fixture['data_factory'](id=1))

    repo.adapter.delete.assert_called_once()
    assert '{} {} with ID 1'.format(
        repo.adapter.delete.__name__,
        repo.agg_root_class.__name__
    ) in caplog.text


def test_delete_batch(caplog, repo_fixture):
    """."""
    count = 5
    repo = repo_fixture['factory']()
    repo.adapter.delete = mock.MagicMock(return_value=None)
    repo.adapter.delete.__name__ = 'delete'
    list_of_dicts = [
        repo_fixture['data_factory'](id='test') for i in range(count)
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
