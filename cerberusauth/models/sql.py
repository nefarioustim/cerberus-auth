"""
SQLAlchemy Models.
"""

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase
from sqlalchemy_utc import UtcDateTime, utcnow

from . import base


class BaseSQLModel(RepresentableBase):
    """Base model for SQLAlchemy."""
    id = Column('id', Integer, primary_key=True)
    created = Column(UtcDateTime, default=utcnow())
    modified = Column(UtcDateTime, onupdate=utcnow())
    is_enabled = Column(Boolean(), default=True)
    is_deleted = Column(Boolean(), default=False)

BaseSQLModel = declarative_base(cls=BaseSQLModel)


class User(BaseSQLModel, base.User):
    """User model for SQLAlchemy."""
    __tablename__ = 'user'

    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    fullname = Column(String(255))

    __init__ = base.User.__init__


class Role(BaseSQLModel, base.Role):
    """Role model for SQLAlchemy."""
    __tablename__ = 'role'

    name = Column(String(255), nullable=False)
    description = Column(String(255))

    __init__ = base.Role.__init__


class Permission(BaseSQLModel, base.Permission):
    """Permission model for SQLAlchemy."""
    __tablename__ = 'permission'

    slug = Column(String(255), nullable=False)
    description = Column(String(255))

    __init__ = base.Permission.__init__
