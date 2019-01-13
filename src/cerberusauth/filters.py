"""
Registration filters for CerberusAuth.
"""

import inspect
from . import models


def filter_model_dict(model_class, model_dict):
    """Filter @model_dict based on @model_class."""
    return_dict = False

    if isinstance(model_dict, dict) and model_dict:
        signature = inspect.signature(model_class.__init__)
        required = [
            param.name for param in signature.parameters.values()
            if param.name != 'self' and
            param.kind == param.POSITIONAL_OR_KEYWORD and
            param.default is param.empty
        ]
        required_keys_in_model_dict = [
            key for key in required if key in model_dict.keys()
        ]

        if required_keys_in_model_dict:
            model_obj = model_class(**{
                key: 'test' for key in required_keys_in_model_dict
            })
            possible = [
                prop for prop in dir(model_obj)
                if not prop.startswith('_') and  # No private properties
                not callable(getattr(model_obj, prop))  # Not callables
            ]
            return_dict = {
                k: model_dict.get(k) for k in possible if model_dict.get(k)
            }

    return return_dict


def filter_user_dict(user_dict):
    """Filter @user_dict based on models.BaseUser."""
    return filter_model_dict(models.BaseUser, user_dict)


def filter_permission_dict(permission_dict):
    """Filter @permission_dict based on models.BasePermission."""
    return filter_model_dict(models.BasePermission, permission_dict)


def filter_role_dict(role_dict):
    """Filter @role_dict based on models.BaseRole."""
    return filter_model_dict(models.BaseRole, role_dict)
