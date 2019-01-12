"""
Models.
"""

import base64
import hashlib
import bcrypt
from slugify import slugify

from .. import authenticate
from .. import config
from .. import strategy


def _import_storage_strategy(storage_strategy=None):
    return strategy.import_strategy(
        storage_strategy or config.STORAGE_STRATEGY,
        '.sql',
        'cerberusauth.models'
    )


def get_user_class(storage_strategy=None):
    return _import_storage_strategy(storage_strategy).User


def get_role_class(storage_strategy=None):
    return _import_storage_strategy(storage_strategy).Role


def get_permission_class(storage_strategy=None):
    return _import_storage_strategy(storage_strategy).Permission


def user_factory(storage_strategy=None, *args, **kwargs):
    return get_user_class(storage_strategy)(*args, **kwargs)


def role_factory(storage_strategy=None, *args, **kwargs):
    return get_role_class(storage_strategy)(*args, **kwargs)


def permission_factory(storage_strategy=None, *args, **kwargs):
    return get_permission_class(storage_strategy)(*args, **kwargs)


# The following provides base classes to derive models from. These base classes
# are not intended for use directly, but instead as parents to modesl for
# specific storage strategies.
#
# TODO: Might be worth converting to AbstractBaseClasses, but I'm not sure how
# that will affect __init__ behaviour. Research required.


class BaseModel(object):
    """Base model."""

    def __init__(self, *args, **kwargs):
        """Constructor."""
        self.id = kwargs.pop("id", None)
        self.created = kwargs.pop("created", None)
        self.modified = kwargs.pop("modified", None)
        self.is_enabled = kwargs.pop("is_enabled", True)
        self.is_deleted = kwargs.pop("is_deleted", False)

        namespace = kwargs.pop("namespace", None)
        self.namespace = slugify(namespace) if namespace else None


class BaseUser(BaseModel):
    """BaseUser model."""

    def __init__(self, email, *args, **kwargs):
        """Constructor."""
        self.email = email
        self.password = kwargs.pop('password', None)
        self.fullname = kwargs.pop('fullname', None)
        self.is_verified = kwargs.pop('is_verified', False)
        self.has_temp_password = kwargs.pop('has_temp_password', False)

        super().__init__(*args, **kwargs)

    @staticmethod
    def _encode_password(password):
        return base64.b64encode(
            hashlib.sha256(
                password.encode("utf-8")
            ).digest()
        )

    def set_password(self, unhashed_password=None):
        """Encode and hash a newly created password."""
        if unhashed_password is None:
            self.has_temp_password = True
            unhashed_password = authenticate.AuthenticateService.get_password()

        else:
            self.has_temp_password = False

        self.password = bcrypt.hashpw(
            self._encode_password(unhashed_password),
            bcrypt.gensalt()
        )

        return unhashed_password

    def authenticate(self, password):
        """Authenticate password matches self.password."""
        return bcrypt.checkpw(
            self._encode_password(password),
            self.password
        )


class BaseRole(BaseModel):
    """BaseRole model."""

    def __init__(self, name, *args, **kwargs):
        """Constructor."""
        self.name = name
        self.description = kwargs.pop("description", None)

        super().__init__(*args, **kwargs)


class BasePermission(BaseModel):
    """BasePermission model."""

    def __init__(self, slug, *args, **kwargs):
        """Constructor."""
        self.slug = slugify(slug)
        self.description = kwargs.pop("description", None)

        super().__init__(*args, **kwargs)
