"""
Authorisation commands for CerberusAuth.
"""

import logging
from ..models import permission_factory
from ..repository import permission


def create_new_permissions_command(session=None, logger=None):
    """NewPermissionsCommand factory."""
    logger = logger or logging.getLogger(__name__)
    return NewPermissionsCommand(
        permission_repository=permission.get_repository(
            session=session, logger=logger),
        logger=logger
    )


class NewPermissionsCommand(object):
    """Command for creating new Permission(s)."""

    def __init__(self, permission_repository, logger=None):
        """Initialise an instance."""
        self.permission_repository = permission_repository
        self.logger = logger

    def __call__(self, *permission_dicts):
        """Add multiple permissions from @permission_dicts."""
        pass
