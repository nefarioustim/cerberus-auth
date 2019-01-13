"""
Authorisation commands for CerberusAuth.
"""

import logging
from .. import filters
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
        filtered_permission_dicts = [
            filters.filter_permission_dict(permission_dict)
            for permission_dict in permission_dicts
            if filters.filter_permission_dict(permission_dict)
        ]

        permissions = self.permission_repository.save(
            *filtered_permission_dicts)

        self.logger.info(
            "Registered {} new Permission(s): {}".format(
                len(filtered_permission_dicts),
                ', '.join([p.slug for p in permissions if p])
            )
        )

        return permissions
