"""
Storage.
"""

from .. import config
from .. import strategy


def get_storage_session(storage_strategy=None):
    """Return Schema class."""
    return strategy.import_strategy(
        storage_strategy or config.STORAGE_STRATEGY,
        '.base',
        'cerberusauth.storage'
    ).get_storage_session()
