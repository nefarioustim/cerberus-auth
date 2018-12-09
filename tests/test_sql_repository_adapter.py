"""
Tests for SQLRepositoryAdapter.
"""

from unittest.mock import Mock
from cerberusauth.repository import sqladapter


class MockSQLModel(Mock):
    """Mock class."""
    id = False


def test_sql_adapter_instantiates(storage_session):
    """."""
    adapter = sqladapter.SQLRepositoryAdapter(storage_session)

    assert adapter
    assert isinstance(adapter, sqladapter.SQLRepositoryAdapter)


def test_sql_adapter_save(storage_session):
    """."""
    adapter = sqladapter.SQLRepositoryAdapter(storage_session)
    thing = Mock()

    added = adapter.save(thing)

    storage_session.add.assert_called_with(thing)
    assert added == thing


def test_repository_count(storage_session):
    """."""
    adapter = sqladapter.SQLRepositoryAdapter(storage_session)

    adapter.count(MockSQLModel)

    storage_session.query.assert_called_once()
    assert storage_session.query.call_args[0][0].__class__.__name__ == 'count'
    query = storage_session.query()
    query.scalar.assert_called_once()


def test_repository_get(storage_session):
    """."""
    adapter = sqladapter.SQLRepositoryAdapter(storage_session)
    adapter.get(MockSQLModel, 1234)

    storage_session.query.assert_called_once()
    storage_session.query.assert_called_with(MockSQLModel)
    query = storage_session.query()
    query.get.assert_called_once()
    # Check passed BinaryExpression using compare method
    assert query.get.call_args[0][0] == 1234


def test_repository_delete(storage_session):
    """."""
    adapter = sqladapter.SQLRepositoryAdapter(storage_session)
    thing = Mock()

    adapter.delete(thing)
    storage_session.delete.assert_called_with(thing)
