"""
Tests for core objects.
"""

from unittest import mock
import cerberusauth
import cerberusauth.schema


def test_cerberus():
    """."""
    cerberus = cerberusauth.cerberus()

    assert cerberus
    assert isinstance(cerberus, cerberusauth.CerberusAuth)
    assert cerberus.register
    assert cerberus.authorise


def test_create_schema(monkeypatch):
    """."""
    create_schema_mock = mock.Mock()
    monkeypatch.setattr(
        cerberusauth.schema, "create_schema", create_schema_mock)

    cerberus = cerberusauth.cerberus()
    cerberus.create_schema()

    create_schema_mock.assert_called_once()
