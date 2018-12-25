"""
SQL storage.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .. import config

engine = create_engine(
    'postgresql://{c.STORAGE_USER}:{c.STORAGE_PASSWORD}@postgres/cerberusauth'
    .format(c=config)
)
Session = sessionmaker(bind=engine)


def get_storage_session():
    """Return a storage session."""
    return Session()
