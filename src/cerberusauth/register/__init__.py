"""
Module containing core functionality for the registration application service.
"""

import logging

from . import command


def create_register_service(session=None, logger=None):
    """RegisterService factory."""
    logger = logger or logging.getLogger(__name__)
    return RegisterService(
        register_users_command=command.create_register_users_command(
            session=session,
            logger=logger
        )
    )


class RegisterService(object):
    """
    An application service that controls all aspects of registration.

    This includes any functionality that can be performed by an anonymous user,
    before they have been authenticated.
    """

    def __init__(self, register_users_command):
        """Initialise RegisterService."""
        self.register_users = register_users_command
