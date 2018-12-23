"""
Datastore schema.
"""

from .. import config
from .. import strategy


def create_schema(storage_strategy=None):
    """Return Schema class."""
    return strategy.import_strategy(
        storage_strategy or config.STORAGE_STRATEGY,
        '.base',
        'cerberusauth.schema'
    ).create_schema()
