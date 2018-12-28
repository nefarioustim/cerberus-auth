"""
Tests for core objects.
"""

import cerberusauth


def test_create_cerberus():
    """."""
    cerberus = cerberusauth.create_cerberus()

    assert cerberus
    assert isinstance(cerberus, cerberusauth.CerberusAuth)
    assert cerberus.registration
