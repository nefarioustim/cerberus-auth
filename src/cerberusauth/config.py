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
SECRET = os.getenv("SECRET", r"""
CX.9kPXH]3wg7brO9z:m"_xYO59:=u:-wjr|qB3~Z5N?1h5DcL1p)6&|}'#q/%p##?tON~Bqn:~9JQjh'*bV$YC{uiDf#H}tZ)5~{GuW.zjkD&M!AhM'OYk&MooM0g
""")
JWT_EXPIRE_SECONDS = os.getenv("JWT_EXPIRE_SECONDS", 86400)
