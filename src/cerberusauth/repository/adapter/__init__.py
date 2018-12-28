"""
Adapters for Repositories.
"""

from ... import config
from ... import strategy


def _import_storage_strategy(storage_strategy=None):
    return strategy.import_strategy(
        storage_strategy or config.STORAGE_STRATEGY,
        '.sql',
        'cerberusauth.repository.adapter'
    )


def get_repository_adapter_class(storage_strategy=None):
    return _import_storage_strategy(
        storage_strategy
    ).get_adapter_class()


def repository_adapter_factory(session, storage_strategy=None):
    return get_repository_adapter_class(storage_strategy)(session)


class RepositoryAdapterInterface(object):
    """Interface for RepositoryAdapter."""

    def commit(self):
        """Commit a change."""
        return None

    def save(self, aggregate_root):
        """Save an aggregate root."""
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
