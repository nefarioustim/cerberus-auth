"""
Test fixtures and configuration for e2e tests.
"""

import pytest
from sqlalchemy import create_engine
import cerberusauth
from cerberusauth.storage import sql as sqlstorage


@pytest.fixture(autouse=True)
def storage_fixture(monkeypatch):
    """Storage fixture for all e2e tests."""
    engine = create_engine('sqlite:///:memory:')
    monkeypatch.setattr(sqlstorage, "engine", engine)


@pytest.fixture
def cerberus_fixture():
    """Session fixture for e2e tests."""
    cerberus = cerberusauth.cerberus()
    cerberus.create_schema()
    return cerberus
