"""
SQLAlchemy Models.
"""

from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utc import UtcDateTime, utcnow

from . import BaseUser, BaseRole, BasePermission


class BaseSQLModel(object):
    """Base model for SQLAlchemy."""
    id = Column('id', Integer, primary_key=True)
    created = Column(UtcDateTime(), default=utcnow())
    modified = Column(UtcDateTime(), default=utcnow(), onupdate=utcnow())
    is_enabled = Column(Boolean(), default=True)
    is_deleted = Column(Boolean(), default=False)

BaseSQLModel = declarative_base(cls=BaseSQLModel)


user_role = Table(
    'userrole', BaseSQLModel.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('role_id', Integer, ForeignKey('role.id'))
)


role_permission = Table(
    'rolepermission', BaseSQLModel.metadata,
    Column('role_id', Integer, ForeignKey('role.id')),
    Column('permission_id', Integer, ForeignKey('permission.id'))
)


class User(BaseSQLModel, BaseUser):
    """User model for SQLAlchemy."""
    __tablename__ = 'user'

    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    fullname = Column(String(255))

    roles = relationship(
        "Role",
        secondary=user_role,
        back_populates="users")

    __init__ = BaseUser.__init__


class Role(BaseSQLModel, BaseRole):
    """Role model for SQLAlchemy."""
    __tablename__ = 'role'

    name = Column(String(255), nullable=False)
    description = Column(String(255))

    users = relationship(
        "User",
        secondary=user_role,
        back_populates="roles")
    permissions = relationship(
        "Permission",
        secondary=role_permission,
        back_populates="roles")

    __init__ = BaseRole.__init__


class Permission(BaseSQLModel, BasePermission):
    """Permission model for SQLAlchemy."""
    __tablename__ = 'permission'

    slug = Column(String(255), nullable=False)
    description = Column(String(255))

    roles = relationship(
        "Role",
        secondary=role_permission,
        back_populates="permissions")

    __init__ = BasePermission.__init__
