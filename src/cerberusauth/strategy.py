"""
Methods for handling strategies.
"""

import importlib


def import_strategy(strategy, default_strategy, strategy_root):
    return importlib.import_module(
        '.{}'.format(strategy if strategy else default_strategy),
        strategy_root
    )
