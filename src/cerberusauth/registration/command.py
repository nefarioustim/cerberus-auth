"""
Registration commands for CerberusAuth.
"""

import logging
from ..repository import user
from . import filters


def create_register_users_command(session=None, logger=None):
    """RegisterUsersCommand factory."""
    logger = logger or logging.getLogger(__name__)
    return RegisterUsersCommand(
        user_repository=user.get_repository(session=session, logger=logger),
        logger=logger
    )


class RegisterUsersCommand(object):
    """Command for registering User(s)."""

    def __init__(self, user_repository, logger=None):
        """Initialise an instance."""
        self.user_repository = user_repository
        self.logger = logger

    def __call__(self, *user_dicts):
        """Register multiple users from @user_dicts."""
        filtered_user_dicts = [
            filters.filter_user_dict(user_dict)
            for user_dict in user_dicts
            if filters.filter_user_dict(user_dict)
        ]
        users = self.user_repository.save(*filtered_user_dicts)

        self.logger.info(
            "Registered {} new User(s): {}".format(
                len(filtered_user_dicts),
                ', '.join([u.email for u in users if u])))

        return users
