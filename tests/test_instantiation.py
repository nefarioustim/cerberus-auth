"""

Tests for core objects.

"""

import cerberusauth


def test_cerberusauth_instantiates():
    """."""
    ca = cerberusauth.CerberusAuth()

    assert ca
