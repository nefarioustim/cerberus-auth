"""
Configuration and fixtures for tests.
"""

from unittest.mock import Mock
import pytest


@pytest.fixture
def storage_session():
    """Mock fixture for session."""
    return Mock()
