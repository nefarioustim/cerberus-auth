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
    """
    Setup logging configuration, to be called on initilisation of application.

    This will attempt to set-up logging based on the configuration file
    logging.yml. This configuration can be overridden by passing the path to a
    similar YAML file as the ENV variable LOGGING_CONFIG_FILE.

    Once set-up, the rest of the microservice can simply create a logging
    instance as normal, with::

        import logging

        logger = logging.getLogger(__name__)

    """
    if os.path.exists(config_path):
        with open(config_path, 'rt') as f:
            logging_config = yaml.safe_load(f.read())

        logging.config.dictConfig(logging_config)
        message = "Logging setup from {}.".format(config_path)

    else:
        logging.basicConfig(level="INFO")
        message = "Logging setup with basicConfig."

    logging.getLogger(__name__).info(message)
