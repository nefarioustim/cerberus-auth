"""
Tests for AuthoriseService.
"""

from cerberusauth import authorise
from cerberusauth.authorise import command


def test_create_authorise_service():
    """."""
    auth = authorise.create_authorise_service()

    assert auth
    assert isinstance(auth, authorise.AuthoriseService)
    assert isinstance(auth.new_permissions, command.NewPermissionsCommand)
