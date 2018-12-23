"""
Tests for SQL get_storage_session.
"""

from sqlalchemy.orm.session import Session
from cerberusauth import storage


def test_get_storage_session():
    """."""
    session = storage.get_storage_session()

    assert session
    assert isinstance(session, Session)
