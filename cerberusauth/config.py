"""
Core configuration for Cerberus.

Any values included in here should be configurable as an environment variable,
so that the service is configurable without code release.
"""

import os


_config_path = os.path.dirname(os.path.realpath(__file__))

LOGGING_CONFIG_FILE = os.getenv(
    "LOGGING_CONFIG_FILE", os.path.join(_config_path, "logging.yml")
)
