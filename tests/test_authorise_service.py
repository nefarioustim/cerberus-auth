"""
Tests for AuthoriseService.
"""

from cerberusauth import authorise


def test_create_authorise_service():
    """."""
    auth = authorise.create_authorise_service()

    assert auth
    assert isinstance(auth, authorise.AuthoriseService)
