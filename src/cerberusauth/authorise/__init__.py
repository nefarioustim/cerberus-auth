"""
Module containing core functionality for the authorisation application service.
"""

import logging


def create_authorise_service(session=None, logger=None):
    """AuthoriseService factory."""
    logger = logger or logging.getLogger(__name__)
    return AuthoriseService()


class AuthoriseService(object):
    """
    An application service that controls all aspects of authorisation.
    """
    pass
