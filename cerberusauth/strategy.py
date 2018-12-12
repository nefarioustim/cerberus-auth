"""
Methods for handling strategies.
"""

import importlib


def import_strategy(strategy, strategy_map, default_strategy, strategy_root):
    return importlib.import_module(
        strategy_map.get(strategy, default_strategy),
        strategy_root
    )
