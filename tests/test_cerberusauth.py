"""
Tests for core objects.
"""

import cerberusauth


def test_cerberus():
    """."""
    cerberus = cerberusauth.cerberus()

    assert cerberus
    assert isinstance(cerberus, cerberusauth.CerberusAuth)
    assert cerberus.registration
