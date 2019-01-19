"""
RepositoryAdapter for SQL storage.
"""

from sqlalchemy import func
from . import RepositoryAdapterInterface


def get_adapter_class():
    return SQLRepositoryAdapter


class SQLRepositoryAdapter(RepositoryAdapterInterface):
    """Repository adapter for SQL storage."""

    def __init__(self, session):
        """Initialise an instance."""
        self.session = session

    def commit(self):
        """Commit a SQLAlchemy change."""
        self.session.commit()

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

    def get_by(self, cls, key, value):
        """Get an aggregate root."""
        return (
            self.session
            .query(cls)
            .filter(getattr(cls, key) == value)
            .first()
        )

    def delete(self, aggregate_root):
        """Delete an aggregate root."""
        self.session.delete(aggregate_root)
