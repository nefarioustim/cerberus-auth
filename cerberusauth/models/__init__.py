"""
Models.
"""

import importlib
from .. import config


STRATEGY_MAP = {
    'sql': 'sqlalchemy',
    'base': 'base'
}


def _import_storage_strategy(storage_strategy=None):
    storage_strategy = storage_strategy or config.STORAGE_STRATEGY
    return importlib.import_module(
        '.{}'.format(STRATEGY_MAP.get(storage_strategy, 'base')),
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
