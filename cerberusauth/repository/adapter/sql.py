"""
RepositoryAdapter for SQL storage.
"""

from sqlalchemy import func
from . import RepositoryAdapterInterface


class SQLRepositoryAdapter(RepositoryAdapterInterface):
    """Repository adapter for SQL storage."""

    def __init__(self, session):
        """Initialise an instance."""
        self.session = session

    def save(self, aggregate_root):
        """Save a SQLAlchemy model."""
        self.session.add(aggregate_root)
        return aggregate_root

    def count(self, cls):
        """Return a count of aggregate roots."""
        return (
            self.session
            .query(func.count(cls.id))
            .scalar()
        )

    def get(self, cls, aggregate_root_id):
        """Get an aggregate root."""
        return (
            self.session
            .query(cls)
            .get(aggregate_root_id)
        )

    def delete(self, aggregate_root):
        """Delete an aggregate root."""
        self.session.delete(aggregate_root)
