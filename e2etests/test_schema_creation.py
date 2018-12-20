"""
Test creation of SQL schema.
"""

import socket
from cerberusauth import schema


def wait_for_postgres():
    """."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False
    while not connected:
        try:
            s.connect(("postgres", "5432"))
            connected = True
        except Exception:
            pass  # Do nothing, just try again


def test_schema_creation():
    """."""
    schema.create_schema()
