"""
Module of core functionality for the authentication application service.
"""

import logging
import xkcdpass.xkcd_password as xp

from . import command

wordfile = xp.locate_wordfile()
words = xp.generate_wordlist(wordfile=wordfile, min_length=5, max_length=8)


def create_authenticate_service(session=None, logger=None):
    """AuthenticateService factory."""
    logger = logger or logging.getLogger(__name__)
    return AuthenticateService(
        authenticate_user_command=command.create_authenticate_user_command(
            session=session,
            logger=logger
        ),
        authenticate_token_command=command.create_authenticate_token_command(
            logger=logger
        )
    )


class AuthenticateService(object):
    """
    An application service that controls all aspects of authentication.
    """

    def __init__(self, authenticate_user_command, authenticate_token_command):
        """Initialise RegisterService."""
        self.authenticate_user = authenticate_user_command
        self.authenticate_token = authenticate_token_command

    @staticmethod
    def get_password():
        """Return password based on @wordlist."""
        return xp.generate_xkcdpassword(words, numwords=5)
