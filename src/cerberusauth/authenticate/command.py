"""
Authentication commands for CerberusAuth.
"""

from datetime import datetime, timedelta
import logging
import jwt
from .. import config
from ..repository import user


def create_authenticate_user_command(session=None, logger=None):
    """AuthenticateUserCommand factory."""
    logger = logger or logging.getLogger(__name__)
    return AuthenticateUserCommand(
        user_repository=user.get_repository(
            session=session, logger=logger),
        logger=logger
    )


class AuthenticateUserCommand(object):
    """
    Command for authenticating a User.

    Checks for existence of user. If found, authenticates password and converts
    user identification payload to a JWT which is returned.
    """

    def __init__(self, user_repository, logger=None):
        """Initialise an instance."""
        self.user_repository = user_repository
        self.logger = logger

    def __call__(self, email, password, expire=None):
        """Load user based on email and authenticate with password."""
        token = False
        expire = int(expire or config.JWT_EXPIRE_SECONDS)
        user = self.user_repository.get_by('email', email)

        if user and user[0] and user[0].authenticate(password):
            token = jwt.encode({
                "id": user[0].id,
                "email": user[0].email,
                "exp": datetime.utcnow() + timedelta(seconds=expire)
            }, config.SECRET)

        return token


def create_authenticate_token_command(logger=None):
    """AuthenticateTokenCommand factory."""
    logger = logger or logging.getLogger(__name__)
    return AuthenticateTokenCommand(logger=logger)


class AuthenticateTokenCommand(object):
    """
    Command for authenticating a token.

    Checks validity of existing token.
    """

    def __init__(self, logger=None):
        """Initialise an instance."""
        self.logger = logger

    def __call__(self, token):
        """Authenticate token."""
        try:
            return_token = jwt.decode(
                token, config.SECRET, algorithms=['HS256'])

        except jwt.InvalidTokenError:
            return_token = False

        return return_token
