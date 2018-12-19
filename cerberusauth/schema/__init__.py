"""
Datastore schema.
"""

from .. import config
from .. import strategy


def get_schema_class(storage_strategy=None):
    """Return Schema class."""
    return strategy.import_strategy(
        storage_strategy or config.STORAGE_STRATEGY,
        '.base',
        'cerberusauth.schema'
    ).Schema


def schema_factory(storage_strategy=None, storage_session=None):
    """Return a Schema object."""
    return get_schema_class(storage_strategy)(storage_session)


class BaseSchema(object):
    """Controls creation of datastore schema."""

    def __init__(self, storage_session=None):
        """Initialise object."""
        self.storage_session = storage_session

    def import_models(self):
        """Import models to create as schema."""
        raise NotImplementedError

    def create_schema(self):
        """Create the schema."""
        raise NotImplementedError
