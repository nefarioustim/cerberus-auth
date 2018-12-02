"""
Base code for models.
"""

from datetime import datetime
import logging


class BaseModel(object):
    """Base model."""
    _initialised = False
    id = None

    def __init__(self, *args, **kwargs):
        """Constructor."""
        self.created = kwargs.pop("created", datetime.utcnow())
        self.modified = kwargs.pop("modified", self.created)

        self._initialised = True


class BaseRepository(object):
    """Provide CRUD behaviour for aggregate roots."""

    AGG_ROOT_CLASS = BaseModel

    def __init__(self, session, logger=None):
        self.session = session
        self.logger = logger or logging.getLogger(__name__)

    def _prepare_aggregate_root(self, aggregate_root):
        if isinstance(aggregate_root, dict):
            aggregate_root = self.AGG_ROOT_CLASS(**aggregate_root)

        return aggregate_root

    def count(self):
        """Return a count of aggregate roots."""
        raise NotImplementedError

    def save(self, *aggregate_roots):
        """Save an aggregate root or roots."""
        raise NotImplementedError

    def get(self, *aggregate_roots):
        """Get an aggregate root or roots."""
        raise NotImplementedError

    def delete(self, *aggregate_roots):
        """Delete an aggregate root or roots."""
        raise NotImplementedError
