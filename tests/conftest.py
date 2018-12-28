"""
Configuration and fixtures for tests.
"""

from unittest.mock import Mock
import pytest


USER_DICT = {
    'email': 'joe.bloggs@gmail.com',
    'password': 'silly password this is',
    'fullname': 'Joe Bloggs'
}

ROLE_DICT = {
    'name': 'Super Admin'
}

PERMISSION_DICT = {
    'slug': 'can-test-permissions'
}


@pytest.fixture
def get_user():
    """Get User dict for testing."""
    def _get_user(id=None):
        return dict(USER_DICT, id=id)
    return _get_user


@pytest.fixture
def get_role():
    """Get Role dict for testing."""
    def _get_role(id=None):
        return dict(ROLE_DICT, id=id)
    return _get_role


@pytest.fixture
def get_permission():
    """Get Permission dict for testing."""
    def _get_permission(id=None):
        return dict(PERMISSION_DICT, id=id)
    return _get_permission


@pytest.fixture
def storage_session():
    """Mock fixture for session."""
    return Mock()
