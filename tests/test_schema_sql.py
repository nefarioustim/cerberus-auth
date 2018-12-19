"""
Tests for datastore schema for SQL.
"""

from cerberusauth import schema


def test_schema_factory():
    """."""
    sql_schema = schema.schema_factory()

    assert sql_schema
    assert isinstance(sql_schema, schema.get_schema_class())
