"""
Repository object for Permission models.
"""

import logging
from . import BaseRepository
from .. import models
from .. import config


def get_repository(logger=None, storage_strategy=None, session=None):
    """PermissionRepository factory."""
    logger = logger or logging.getLogger(__name__)
    storage_strategy = storage_strategy or config.STORAGE_STRATEGY
    return PermissionRepository(
        logger=logger,
        storage_strategy=storage_strategy,
        session=session
    )


class PermissionRepository(BaseRepository):
    """Provide CRUD behaviour for aggregate roots."""

    def __init__(self, logger, storage_strategy, session=None):
        super(PermissionRepository, self).__init__(
            logger, storage_strategy, session)
        self.agg_root_class = models.get_permission_class(
            self.storage_strategy)
