"""
Tests for RepositoryAdapter interface.
"""

from unittest.mock import Mock
import pytest
from cerberusauth.repository import adapter


def test_interface_has_commit():
    """."""
    interface = adapter.RepositoryAdapterInterface()

    assert interface.commit() is None


def test_interface_has_save():
    """."""
    interface = adapter.RepositoryAdapterInterface()

    with pytest.raises(NotImplementedError):
        interface.save(Mock())


def test_interface_has_count():
    """."""
    interface = adapter.RepositoryAdapterInterface()

    with pytest.raises(NotImplementedError):
        interface.count()


def test_interface_has_get():
    """."""
    interface = adapter.RepositoryAdapterInterface()

    with pytest.raises(NotImplementedError):
        interface.get(1234)


def test_interface_has_delete():
    """."""
    interface = adapter.RepositoryAdapterInterface()

    with pytest.raises(NotImplementedError):
        interface.delete(Mock())
