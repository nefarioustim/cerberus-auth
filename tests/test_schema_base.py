"""
Tests for Schema interface.
"""

import pytest
from cerberusauth import schema


def test_interface_has_import_models():
    """."""
    schema_obj = schema.BaseSchema()

    with pytest.raises(NotImplementedError):
        schema_obj.import_models()


def test_interface_has_create_schema():
    """."""
    schema_obj = schema.BaseSchema()

    with pytest.raises(NotImplementedError):
        schema_obj.create_schema()
