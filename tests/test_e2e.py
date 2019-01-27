"""
E2E tests for CerberusAuth.
"""

import pytest

USERS_JSON = """
[
  {"email": "someone@something"},
  {"email": "someoneelse@something"}
]
"""


@pytest.mark.e2etest
def test_service_creation(e2e_cerberus_fixture):
    """."""
    cerberus = e2e_cerberus_fixture

    assert cerberus


@pytest.mark.e2etest
def test_e2e_register_users(e2e_cerberus_fixture):
    """."""
    cerberus = e2e_cerberus_fixture

    response = cerberus.register_users(USERS_JSON)

    assert response
