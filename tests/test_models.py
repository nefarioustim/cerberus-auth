"""
Tests for models.
"""

import pytest

from cerberusauth import models as base_models

from .model_tests import *


@pytest.fixture
def models():
    """Models fixture."""
    return base_models
