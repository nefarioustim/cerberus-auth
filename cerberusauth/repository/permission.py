"""
Repository object for Permission models.
"""

import logging
from . import adapter
from .. import models
from .. import config


def get_repository(session=None, storage_strategy=None, logger=None):
    """PermissionRepository factory."""
    return PermissionRepository(
        session=session,
        storage_strategy=storage_strategy,
        logger=logger
    )


class PermissionRepository(object):
    """Provide CRUD behaviour for aggregate roots."""

    def __init__(self, session=None, storage_strategy=None, logger=None):
        self.storage_strategy = storage_strategy or config.STORAGE_STRATEGY
        self.agg_root_class = models.get_permission_class(
            storage_strategy)
        self.adapter = adapter.repository_adapter_factory(
            session, storage_strategy)
        self.logger = logger or logging.getLogger(__name__)

    def get_aggregate_root_object(self, agg_root):
        if isinstance(agg_root, dict):
            agg_root = self.agg_root_class(**agg_root)

        return agg_root

    def count(self):
        """Return a count of aggregate roots."""
        return self.adapter.count(self.agg_root_class)

    def _get(self, agg_root_id):
        agg_root = self.adapter.get(self.agg_root_class, agg_root_id)
        self.logger.info('Got {} with ID {}'.format(
            self.agg_root_class.__name__, agg_root_id))
        return agg_root

    def get(self, *aggregate_root_ids):
        """Get an aggregate root or roots."""
        return [
            self._get(agg_root_id) for agg_root_id in aggregate_root_ids
        ]

    def save(self, *aggregate_roots):
        """Save an aggregate root or roots."""
        return [
            self.adapter.save(
                self.get_aggregate_root_object(agg_root)
            ) for agg_root in aggregate_roots
        ]

    def delete(self, *aggregate_roots):
        """Delete an aggregate root or roots."""
        for agg_root in aggregate_roots:
            self.adapter.delete(
                self.get_aggregate_root_object(agg_root)
            )
