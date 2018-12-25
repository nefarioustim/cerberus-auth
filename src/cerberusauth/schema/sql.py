"""
Datastore schema for SQL.
"""

from ..storage import sql as sqlstorage


def create_schema():
    """Create the schema."""
    from ..models import sql as sqlmodels

    sqlmodels.BaseSQLModel.metadata.create_all(sqlstorage.engine)
