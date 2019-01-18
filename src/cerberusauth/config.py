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
STORAGE_STRATEGY = os.getenv("STORAGE_STRATEGY", "sql")
STORAGE_USER = os.getenv("STORAGE_USER", None)
STORAGE_PASSWORD = os.getenv("STORAGE_PASSWORD", None)
SMTP_USER = os.getenv("SMTP_USER", None)
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", None)
SECRET = os.getenv("SECRET", None)
JWT_EXPIRE_SECONDS = os.getenv("JWT_EXPIRE_SECONDS", 86400)
