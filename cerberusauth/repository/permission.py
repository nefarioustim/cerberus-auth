"""
Repository object for Permission models.
"""

import logging
from . import adapter


def get_repository(session=None, adapter_obj=None):
    """PermissionRepository factory."""
    return PermissionRepository(
        adapter=adapter_obj or adapter.repository_adapter_factory(session)
    )


class PermissionRepository(object):
    """Provide CRUD behaviour for aggregate roots."""

    def __init__(self, adapter, logger=None):
        self.adapter = adapter
        self.logger = logger or logging.getLogger(__name__)

    @staticmethod
    def _prepare_aggregate_root(agg_root_class, agg_root):
        if isinstance(agg_root, dict):
            agg_root = agg_root_class(**agg_root)

        return agg_root

    def count(self):
        """Return a count of aggregate roots."""
        raise NotImplementedError

    def save(self, *aggregate_roots):
        """Save an aggregate root or roots."""
        raise NotImplementedError

    def get(self, *aggregate_roots):
        """Get an aggregate root or roots."""
        raise NotImplementedError

    def delete(self, *aggregate_roots):
        """Delete an aggregate root or roots."""
        raise NotImplementedError
