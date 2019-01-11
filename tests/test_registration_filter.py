"""
Tests for registration filters.
"""

import pytest
from cerberusauth.registration import filters


@pytest.mark.parametrize("user_dict, expected", ((
    {'email': 'test'}, {'email': 'test'}
), (
    {'email': 'test', 'fullname': 'geoff'},
    {'email': 'test', 'fullname': 'geoff'}
), (
    {'fullname': 'geoff'},
    False
), (
    True,
    False
), (
    "Geoffrey!",
    False
)))
def test_filter_user_dict(user_dict, expected):
    """."""
    filtered = filters.filter_user_dict(user_dict)

    assert filtered == expected
