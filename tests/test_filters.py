"""
Tests for registration filters.
"""

import pytest
from cerberusauth import filters


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


@pytest.mark.parametrize("permission_dict, expected", ((
    {'slug': 'Wonky Donky'}, {'slug': 'Wonky Donky'}
), (
    {'slug': 'test', 'description': 'geoff'},
    {'slug': 'test', 'description': 'geoff'}
), (
    {'name': 'Wonky Donky'},
    False
), (
    True,
    False
), (
    "Geoffrey!",
    False
)))
def test_filter_permission_dict(permission_dict, expected):
    """."""
    filtered = filters.filter_permission_dict(permission_dict)

    assert filtered == expected
