"""
Cerberus - Authentication and authorisation microservice.
"""

from . import config
from . import register
from . import schema
from . import storage


def cerberus():
    return CerberusAuth(
        storage_strategy=config.STORAGE_STRATEGY
    )


class CerberusAuth(object):
    """
    Provides authentication and authorisation as a microservice.
    """

    def __init__(self, storage_strategy):
        """Initialise an instance."""
        self.storage_strategy = storage_strategy

        self._setup_storage()
        self._setup_services()

    def _setup_storage(self):
        """Setup storage from self.storage_strategy."""
        self.has_storage_session = storage.has_storage_session(
            self.storage_strategy)
        self.storage_session = storage.get_storage_session(
            self.storage_strategy) if self.has_storage_session else None

    def _setup_services(self):
        """Setup services with self.storage_session."""
        self.register = register.create_register_service(
            session=self.storage_session)

    def create_schema(self):
        """Create storage schema."""
        schema.create_schema()
