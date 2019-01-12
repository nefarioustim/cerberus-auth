"""
Module containing core functionality for the authorisation application service.
"""

import logging

from . import command


def create_authorise_service(session=None, logger=None):
    """AuthoriseService factory."""
    logger = logger or logging.getLogger(__name__)
    return AuthoriseService(
        new_permissions_command=command.create_new_permissions_command(
            session=session,
            logger=logger
        )
    )


class AuthoriseService(object):
    """
    An application service that controls all aspects of authorisation.
    """

    def __init__(self, new_permissions_command):
        """Initialise RegisterService."""
        self.new_permissions = new_permissions_command
