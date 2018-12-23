"""
Tests for SQL create_schema.
"""

from unittest import mock
from cerberusauth import schema
from cerberusauth.storage import sql


def test_create_schema(monkeypatch):
    """."""
    engine_mock = mock.Mock()
    monkeypatch.setattr(sql, 'engine', engine_mock)
    schema.create_schema()

    assert engine_mock.method_calls
