"""
Tests for version file.
"""


def test_version_imports():
    """."""
    from cerberusauth import __version__ as version

    assert version
