"""
Tests for core objects.
"""

import cerberusauth


def test_cerberusauth_factory():
    """."""
    cerberus = cerberusauth.create_cerberus()

    assert cerberus
    assert isinstance(cerberus, cerberusauth.CerberusAuth)
