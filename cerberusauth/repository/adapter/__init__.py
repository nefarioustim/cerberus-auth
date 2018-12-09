"""
Adapters for Repositories.
"""


class RepositoryAdapterInterface(object):
    """Interface for RepositoryAdapter."""

    def save(self, aggregate_root):
        """Save a SQLAlchemy model."""
        raise NotImplementedError

    def count(self):
        """Return a count of aggregate roots."""
        raise NotImplementedError

    def get(self, aggregate_root_id):
        """Get an aggregate root."""
        raise NotImplementedError

    def delete(self, aggregate_root):
        """Delete an aggregate root."""
        raise NotImplementedError
