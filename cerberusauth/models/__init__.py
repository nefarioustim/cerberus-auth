"""
Models.
"""

from .. import config
from . import base
from . import sqlalchemy


STRATEGY_MAP = {
    'sql': 'sqlalchemy',
    'base': 'base'
}


def _get_storage_strategy(storage_strategy=None):
    storage_strategy = storage_strategy or config.STORAGE_STRATEGY
    return globals().get(
        STRATEGY_MAP.get(storage_strategy, 'base'),
        'base'
    )


def get_user_class(storage_strategy=None):
    return _get_storage_strategy(storage_strategy).User


def get_role_class(storage_strategy=None):
    return _get_storage_strategy(storage_strategy).Role


def get_permission_class(storage_strategy=None):
    return _get_storage_strategy(storage_strategy).Permission


def user_factory(storage_strategy=None, *args, **kwargs):
    return get_user_class(storage_strategy)(*args, **kwargs)


def role_factory(storage_strategy=None, *args, **kwargs):
    return get_role_class(storage_strategy)(*args, **kwargs)


def permission_factory(storage_strategy=None, *args, **kwargs):
    return get_permission_class(storage_strategy)(*args, **kwargs)
