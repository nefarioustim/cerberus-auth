"""
Authorisation commands for CerberusAuth.
"""

import logging
from .. import filters
from ..repository import permission, role


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


def create_new_roles_command(session=None, logger=None):
    """NewRolesCommand factory."""
    logger = logger or logging.getLogger(__name__)
    return NewRolesCommand(
        role_repository=role.get_repository(
            session=session, logger=logger),
        logger=logger
    )


class NewRolesCommand(object):
    """Command for creating new Role(s)."""

    def __init__(self, role_repository, logger=None):
        """Initialise an instance."""
        self.role_repository = role_repository
        self.logger = logger

    def __call__(self, *role_dicts):
        """Add multiple roles from @role_dicts."""
        filtered_role_dicts = [
            filters.filter_role_dict(role_dict)
            for role_dict in role_dicts
            if filters.filter_role_dict(role_dict)
        ]

        roles = self.role_repository.save(
            *filtered_role_dicts)

        self.logger.info(
            "Registered {} new Role(s): {}".format(
                len(filtered_role_dicts),
                ', '.join([r.name for r in roles if r])
            )
        )

        return roles
