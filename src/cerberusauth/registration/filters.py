"""
Registration filters for CerberusAuth.
"""

import inspect
from .. import models


def filter_user_dict(user_dict):
    """Filter @user_dict based on models.BaseUser."""
    return_dict = False

    if isinstance(user_dict, dict) and user_dict:
        signature = inspect.signature(models.BaseUser.__init__)
        required = [
            param.name for param in signature.parameters.values()
            if param.name != 'self' and
            param.kind == param.POSITIONAL_OR_KEYWORD and
            param.default is param.empty
        ]
        required_keys_in_user_dict = [
            key for key in required if key in user_dict.keys()
        ]

        if required_keys_in_user_dict:
            user_obj = models.BaseUser(email='test')
            possible = [
                prop for prop in dir(user_obj)
                if not prop.startswith('_') and  # No private properties
                not callable(getattr(user_obj, prop))  # Not callables
            ]
            return_dict = {
                k: user_dict.get(k) for k in possible if user_dict.get(k)
            }

    return return_dict
