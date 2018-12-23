"""
Data for use across tests.
"""

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


def get_user(id=None):
    """Get User dict for testing."""
    return dict(USER_DICT, id=id)


def get_role(id=None):
    """Get User dict for testing."""
    return dict(ROLE_DICT, id=id)


def get_permission(id=None):
    """Get User dict for testing."""
    return dict(PERMISSION_DICT, id=id)
