"""
Storage.
"""

from .. import config
from .. import strategy

STORAGE_MAP = {
    'sql': {
        'has_storage_session': True
    }
}


def has_storage_session(storage_strategy=None):
    """Return boolean flagging the need for a storage session."""
    return bool(
        STORAGE_MAP[storage_strategy or config.STORAGE_STRATEGY]
        .get('has_storage_session', True)
    )


def get_storage_session(storage_strategy=None):
    """Return Schema class."""
    return strategy.import_strategy(
        storage_strategy or config.STORAGE_STRATEGY,
        '.base',
        'cerberusauth.storage'
    ).get_storage_session()
