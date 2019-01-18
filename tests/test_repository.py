"""Tests for PermissionRepository."""

from unittest import mock

import pytest

from cerberusauth.repository import permission, role, user
from cerberusauth.repository.adapter import RepositoryAdapterInterface
from cerberusauth.repository.adapter import sql
from cerberusauth import models
from cerberusauth.models import sql as sql_models


@pytest.fixture(params=[{
    'factory': permission.get_repository,
    'repo_class': permission.PermissionRepository,
    'repo_adapter_class': sql.SQLRepositoryAdapter,
    'base_model_class': models.BasePermission,
    'model_class': sql_models.Permission
}, {
    'factory': role.get_repository,
    'repo_class': role.RoleRepository,
    'repo_adapter_class': sql.SQLRepositoryAdapter,
    'base_model_class': models.BaseRole,
    'model_class': sql_models.Role
}, {
    'factory': user.get_repository,
    'repo_class': user.UserRepository,
    'repo_adapter_class': sql.SQLRepositoryAdapter,
    'base_model_class': models.BaseUser,
    'model_class': sql_models.User
}], ids=["permission", "role", "user"])
def repo_fixture(request, get_permission, get_role, get_user):
    """Fixture for repo tests."""
    if request.param['model_class'] == sql_models.Permission:
        request.param['data_factory'] = get_permission
    elif request.param['model_class'] == sql_models.Role:
        request.param['data_factory'] = get_role
    elif request.param['model_class'] == sql_models.User:
        request.param['data_factory'] = get_user
    return request.param


def test_repository_factory(repo_fixture):
    """."""
    repo = repo_fixture['factory']()

    assert repo
    assert isinstance(repo, repo_fixture['repo_class'])
    assert isinstance(repo.adapter, RepositoryAdapterInterface)
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
    assert isinstance(agg_root, repo_fixture['model_class'])
    assert isinstance(agg_root, repo_fixture['base_model_class'])

    # Assert sending it an aggregate root object also works.
    agg_root = repo.get_aggregate_root_object(agg_root)

    assert agg_root
    assert isinstance(agg_root, repo.agg_root_class)
    assert isinstance(agg_root, repo_fixture['model_class'])
    assert isinstance(agg_root, repo_fixture['base_model_class'])


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


def test_get_by(caplog, repo_fixture):
    """."""
    repo = repo_fixture['factory']()
    repo.adapter.get_by = mock.Mock()

    with caplog.at_level("INFO"):
        repo.get_by({'email': 'something'})

    repo.adapter.get_by.assert_called_once_with(
        repo.agg_root_class, 'email', 'something')
    assert 'Got {} with email something'.format(
        repo.agg_root_class.__name__
    ) in caplog.text


def test_get_by_batch(caplog, repo_fixture):
    """."""
    test_dicts = [
        {'email': 'something'},
        {'email': 'geoff'},
        {'foo': 'bar'},
        {'fullname': 'Geoff Jefferson'}
    ]
    repo = repo_fixture['factory']()
    repo.adapter.get_by = mock.Mock()

    with caplog.at_level("INFO"):
        repo.get_by(*test_dicts)

    for test_dict in test_dicts:
        (key, value) = list(test_dict.items())[0]
        repo.adapter.get_by.assert_any_call(repo.agg_root_class, key, value)
        assert 'Got {} with {} {}'.format(
            repo.agg_root_class.__name__, key, value
        ) in caplog.text


def test_save(caplog, repo_fixture):
    """."""
    repo = repo_fixture['factory']()
    return_perm = repo.get_aggregate_root_object(
        repo_fixture['data_factory']())
    return_perm.id = 1
    repo.adapter = mock.MagicMock()
    repo.adapter.save.__name__ = 'save'
    repo.adapter.save.return_value = return_perm
    repo.adapter.commit = mock.Mock()

    with caplog.at_level("INFO"):
        repo.save(repo_fixture['data_factory']())

    repo.adapter.save.assert_called_once()
    assert '{} {} with ID 1'.format(
        repo.adapter.save.__name__,
        repo.agg_root_class.__name__
    ) in caplog.text
    repo.adapter.commit.assert_called_once()


def test_save_batch(repo_fixture):
    """."""
    count = 5
    repo = repo_fixture['factory']()
    repo.adapter = mock.Mock()
    repo.adapter.commit = mock.Mock()
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
    repo.adapter = mock.MagicMock()
    repo.adapter.delete.__name__ = 'delete'
    repo.adapter.delete.return_value = None
    repo.adapter.commit = mock.Mock()

    with caplog.at_level("INFO"):
        repo.delete(repo_fixture['data_factory'](id=1))

    repo.adapter.delete.assert_called_once()
    assert '{} {} with ID 1'.format(
        repo.adapter.delete.__name__,
        repo.agg_root_class.__name__
    ) in caplog.text
    repo.adapter.commit.assert_called_once()


def test_delete_batch(caplog, repo_fixture):
    """."""
    count = 5
    repo = repo_fixture['factory']()
    repo.adapter = mock.MagicMock()
    repo.adapter.delete.__name__ = 'delete'
    repo.adapter.delete.return_value = None
    repo.adapter.commit = mock.Mock()
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
