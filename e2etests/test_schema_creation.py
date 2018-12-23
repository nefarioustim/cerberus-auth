"""
Test creation of SQL schema.
"""

import pytest
from sqlalchemy.inspection import inspect
from cerberusauth.schema import sql as sqlschema
from cerberusauth.models import sql as sqlmodels

EXPECTED_MODELS = ['user', 'role', 'permission']


@pytest.fixture
def inspection_engine():
    """Drops schema at end of test."""
    engine = sqlschema.sqlstorage.engine
    yield inspect(engine)
    sqlmodels.BaseSQLModel.metadata.drop_all(engine)


def test_schema_creation(inspection_engine):
    """."""
    sqlschema.create_schema()

    assert inspection_engine.get_table_names() == EXPECTED_MODELS
