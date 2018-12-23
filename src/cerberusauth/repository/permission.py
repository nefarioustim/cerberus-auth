"""
Repository object for Permission models.
"""

import logging
from . import BaseRepository, adapter
from .. import models
from .. import config


def get_repository(session=None, storage_strategy=None, logger=None):
    """PermissionRepository factory."""
    return PermissionRepository(
        session=session,
        storage_strategy=storage_strategy,
        logger=logger
    )


class PermissionRepository(BaseRepository):
    """Provide CRUD behaviour for aggregate roots."""

    def __init__(self, session=None, storage_strategy=None, logger=None):
        self.storage_strategy = storage_strategy or config.STORAGE_STRATEGY
        self.agg_root_class = models.get_permission_class(
            storage_strategy)
        self.adapter = adapter.repository_adapter_factory(
            session, storage_strategy)
        self.logger = logger or logging.getLogger(__name__)
