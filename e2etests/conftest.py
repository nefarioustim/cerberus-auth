"""
Test fixtures and configuration for e2e tests.
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import cerberusauth
from cerberusauth.storage import sql as sqlstorage


@pytest.fixture(autouse=True)
def storage_fixture(monkeypatch):
    """Storage fixture for all e2e tests."""
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)

    monkeypatch.setattr(sqlstorage, "engine", engine)
    monkeypatch.setattr(sqlstorage, "Session", Session)


@pytest.fixture
def cerberus_fixture(storage_fixture):
    """Session fixture for e2e tests."""
    cerberus = cerberusauth.cerberus()
    cerberus.create_schema()
    return cerberus
