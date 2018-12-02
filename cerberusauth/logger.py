"""
Logging set-up for Cerberus.
"""

import os
import logging.config

import yaml

from . import config


def setup_logging(
    config_path=config.LOGGING_CONFIG_FILE
):
    """Setup logging configuration."""
    if os.path.exists(config_path):
        with open(config_path, 'rt') as f:
            logging_config = yaml.safe_load(f.read())

        logging.config.dictConfig(logging_config)
        message = "Logging setup from {}.".format(config_path)

    else:
        logging.basicConfig(level="INFO")
        message = "Logging setup with basicConfig."

    logging.getLogger(__name__).info(message)
