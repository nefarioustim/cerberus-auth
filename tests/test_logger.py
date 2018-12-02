"""
Tests for logging setup.
"""

from cerberusauth import logger


def test_setup_logging(caplog):
    """."""
    with caplog.at_level("INFO"):
        logger.setup_logging()

    assert "Logging setup from /app/cerberusauth/logging.yml." in caplog.text


def test_setup_logging_with_bad_config(caplog):
    """."""
    with caplog.at_level("INFO"):
        logger.setup_logging("geoff")

    assert "Logging setup with basicConfig." in caplog.text
