"""
Models.
"""

import base64
from datetime import datetime
import hashlib
import bcrypt
from slugify import slugify


class BaseModel(object):
    """Base model."""
    _initialised = False
    id = None

    def __init__(self, *args, **kwargs):
        """Constructor."""
        self.created = kwargs.pop("created", datetime.utcnow())
        self.modified = kwargs.pop("created", self.created)

        self._initialised = True

    def __setattr__(self, name, value):
        """Global setter."""
        if not name == "modified" and self._initialised:
            self.modified = datetime.utcnow()

        super(BaseModel, self).__setattr__(name, value)


class User(BaseModel):
    """User model."""

    def __init__(self, email, password=None, fullname=None, *args, **kwargs):
        """Constructor."""
        self.email = email
        self.password = password
        self.fullname = fullname

        super(User, self).__init__(
            *args, **kwargs
        )

    @staticmethod
    def _encode_password(password):
        return base64.b64encode(
            hashlib.sha256(
                password.encode("utf-8")
            ).digest()
        )

    def new_password(self, unhashed_password):
        """Encode and hash a newly created password."""
        self.password = bcrypt.hashpw(
            self._encode_password(unhashed_password),
            bcrypt.gensalt()
        )

    def authenticate(self, password):
        """Authenticate password matches self.password."""
        return bcrypt.checkpw(
            self._encode_password(password),
            self.password
        )


class Role(BaseModel):
    """Role model."""

    def __init__(self, name, *args, **kwargs):
        """Constructor."""
        self.name = name
        self.description = kwargs.pop("description", None)
        self.enabled = kwargs.pop("enabled", True)

        super(Role, self).__init__(
            *args, **kwargs
        )


class Permission(BaseModel):
    """Permission model."""

    def __init__(self, slug, *args, **kwargs):
        """Constructor."""
        self.slug = slugify(slug)
        self.description = kwargs.pop("description", None)
        self.enabled = kwargs.pop("enabled", True)

        super(Permission, self).__init__(
            *args, **kwargs
        )
