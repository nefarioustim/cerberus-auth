"""
Registration application service.
"""

import logging

from . import command


def create_registration_service(session=None, logger=None):
    """RegistrationService factory."""
    logger = logger or logging.getLogger(__name__)
    return RegistrationService(
        register_users_command=command.create_register_users_command(
            session=session,
            logger=logger
        )
    )


class RegistrationService(object):
    """Registration application service."""

    def __init__(self, register_users_command):
        """Initialise RegistrationService."""
        self.register_users = register_users_command
