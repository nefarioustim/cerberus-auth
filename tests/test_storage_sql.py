"""
Tests for SQL get_storage_session.
"""

import pytest

from sqlalchemy.orm.session import Session
from cerberusauth import storage


@pytest.mark.parametrize("storage_strategy", (False, "sql"))
def test_has_storage_session(storage_strategy):
    """."""
    assert storage.has_storage_session(storage_strategy)


def test_get_storage_session():
    """."""
    session = storage.get_storage_session()

    assert session
    assert isinstance(session, Session)
