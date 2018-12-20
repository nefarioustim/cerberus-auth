"""
Datastore schema for SQL.
"""


def create_schema():
    """Create the schema."""
    from ..models import sql as sqlmodels
    from ..storage import sql as sqlstorage

    sqlmodels.BaseSQLModel.metadata.create_all(sqlstorage.engine)
