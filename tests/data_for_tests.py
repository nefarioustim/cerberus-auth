"""
Data for use across tests.
"""

USER_DICT = {
    'email': 'joe.bloggs@gmail.com',
    'password': 'silly password this is',
    'fullname': 'Joe Bloggs'
}

ROLE_DICT = {
    'name': 'Super Admin',
    'enabled': True
}

PERMISSION_DICT = {
    'slug': 'can-test-permissions',
    'enabled': True
}


def get_user():
    """Get User dict for testing."""
    return USER_DICT.copy()


def get_role():
    """Get User dict for testing."""
    return ROLE_DICT.copy()


def get_permission():
    """Get User dict for testing."""
    return PERMISSION_DICT.copy()
