"""
Marshmallow serialization schemas for models.
"""

from marshmallow import Schema, fields


class BaseSchema(Schema):
    id = fields.Str()
    created = fields.DateTime()
    modified = fields.DateTime()
    is_enabled = fields.Boolean()
    is_deleted = fields.Boolean()
    namespace = fields.Str()


class UserSchema(BaseSchema):
    email = fields.Email()
    fullname = fields.Str()
    is_verified = fields.Boolean()
    has_temp_password = fields.Boolean()


class RegisteredUserSchema(Schema):
    user = fields.Nested(UserSchema)
    temp_password = fields.Str()


class RoleSchema(BaseSchema):
    name = fields.Str()
    description = fields.Str()


class PermissionSchema(BaseSchema):
    slug = fields.Str()
    description = fields.Str()
