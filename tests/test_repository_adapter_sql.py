"""
Tests for SQLRepositoryAdapter.
"""

from unittest.mock import Mock
from cerberusauth.repository.adapter import sql as sqladapter


class MockSQLModel(Mock):
    """Mock class."""
    id = False
    email = 'something'


def test_sql_adapter_instantiates(storage_session):
    """."""
    adapter = sqladapter.SQLRepositoryAdapter(storage_session)

    assert adapter
    assert isinstance(adapter, sqladapter.SQLRepositoryAdapter)


def test_sql_adapter_commit(storage_session):
    """."""
    adapter = sqladapter.SQLRepositoryAdapter(storage_session)

    adapter.commit()

    storage_session.commit.assert_called_once()


def test_sql_adapter_save(storage_session):
    """."""
    adapter = sqladapter.SQLRepositoryAdapter(storage_session)
    thing = Mock()

    added = adapter.save(thing)

    storage_session.add.assert_called_with(thing)
    assert added == thing


def test_sql_adapter_count(storage_session):
    """."""
    adapter = sqladapter.SQLRepositoryAdapter(storage_session)

    adapter.count(MockSQLModel)

    storage_session.query.assert_called_once()
    assert storage_session.query.call_args[0][0].__class__.__name__ == 'count'
    query = storage_session.query()
    query.scalar.assert_called_once()


def test_sql_adapter_get(storage_session):
    """."""
    adapter = sqladapter.SQLRepositoryAdapter(storage_session)
    adapter.get(MockSQLModel, 1234)

    storage_session.query.assert_called_once()
    storage_session.query.assert_called_with(MockSQLModel)
    query = storage_session.query()
    query.get.assert_called_once()
    # Check passed BinaryExpression using compare method
    assert query.get.call_args[0][0] == 1234


def test_sql_adapter_get_by(storage_session):
    """."""
    adapter = sqladapter.SQLRepositoryAdapter(storage_session)
    adapter.get_by(MockSQLModel, 'email', 'something')

    storage_session.query.assert_called_once()
    storage_session.query.assert_called_with(MockSQLModel)
    query = storage_session.query()
    query.filter.assert_called_with(MockSQLModel.email == 'something')
    query_filter = query.filter()
    query_filter.first.assert_called_once()


def test_sql_adapter_delete(storage_session):
    """."""
    adapter = sqladapter.SQLRepositoryAdapter(storage_session)
    thing = Mock()

    adapter.delete(thing)
    storage_session.delete.assert_called_with(thing)
