"""
Cerberus - Authentication and authorisation microservice.
"""

import simplejson as json

from . import authenticate
from . import authorise
from . import config
from . import register
from . import schema
from . import storage

from .models.serial import RegisteredUserSchema


class CerberusAuth(object):
    """
    Provides authentication and authorisation as a microservice.
    """

    def __init__(self):
        """Initialise an instance."""
        self.storage_strategy = config.STORAGE_STRATEGY

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
        self.authenticate = authenticate.create_authenticate_service(
            session=self.storage_session)
        self.authorise = authorise.create_authorise_service(
            session=self.storage_session)
        self.register = register.create_register_service(
            session=self.storage_session)

    def create_schema(self):
        """Create storage schema."""
        schema.create_schema(self.storage_strategy)

    def register_users(self, users_json):
        """Register multiple users from @users_json."""
        user_dicts = json.loads(users_json)
        users = self.register.register_users(*user_dicts)
        users = RegisteredUserSchema().dumps(
            users, many=True, sort_keys=True, indent=2 * ' ')
        return users.data
