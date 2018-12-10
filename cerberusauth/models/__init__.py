"""
Models.
"""

from . import base
from . import sqlalchemy


def get_user_class(storage_strategy=None):
    return (
        sqlalchemy.User if storage_strategy == 'sql'
        else base.User
    )


def get_role_class(storage_strategy=None):
    return (
        sqlalchemy.Role if storage_strategy == 'sql'
        else base.Role
    )


def get_permission_class(storage_strategy=None):
    return (
        sqlalchemy.Permission if storage_strategy == 'sql'
        else base.Permission
    )


def user_factory(storage_strategy=None, *args, **kwargs):
    return get_user_class(storage_strategy)(*args, **kwargs)


def role_factory(storage_strategy=None, *args, **kwargs):
    return get_role_class(storage_strategy)(*args, **kwargs)


def permission_factory(storage_strategy=None, *args, **kwargs):
    return get_permission_class(storage_strategy)(*args, **kwargs)
