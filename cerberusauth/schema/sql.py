"""
Datastore schema for SQL.
"""

from . import BaseSchema


class Schema(BaseSchema):
    """Controls creation of datastore schema."""

    def import_models(self):
        """Import models to create as schema."""

    def create_schema(self):
        """Create the schema."""
