"""
E2E tests.
"""

from sqlalchemy.inspection import inspect
from cerberusauth.schema import sql as sqlschema

EXPECTED_MODELS = ['user', 'role', 'permission']


def test_schema_creation(cerberus_fixture):
    """."""
    assert "sqlite" in str(sqlschema.sqlstorage.engine)
    iengine = inspect(sqlschema.sqlstorage.engine)

    assert set(iengine.get_table_names()) == set(EXPECTED_MODELS)
