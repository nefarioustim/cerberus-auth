"""
Module of core functionality for the authentication application service.
"""

import logging
import xkcdpass.xkcd_password as xp

wordfile = xp.locate_wordfile()
words = xp.generate_wordlist(wordfile=wordfile, min_length=5, max_length=8)


def create_authenticate_service(session=None, logger=None):
    """AuthenticateService factory."""
    logger = logger or logging.getLogger(__name__)
    return AuthenticateService()


class AuthenticateService(object):
    """
    An application service that controls all aspects of authentication.
    """

    @staticmethod
    def get_password():
        """Return password based on @wordlist."""
        return xp.generate_xkcdpassword(words, numwords=5)