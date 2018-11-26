"""
Models.
"""

from slugify import slugify


class User(object):
    """User model."""

    def __init__(self, email, password, fullname, *args, **kwargs):
        """Constructor."""
        self.email = email
        self.password = password
        self.fullname = fullname

        # super(User, self).__init__(
        #     email=email,
        #     password=password,
        #     fullname=fullname,
        #     *args, **kwargs
        # )


class Role(object):
    """Role model."""

    def __init__(self, name, *args, **kwargs):
        """Constructor."""
        self.name = name
        self.description = kwargs.pop('description', None)
        self.enabled = kwargs.pop('enabled', True)

        # super(Role, self).__init__(
        #     name=name,
        #     *args, **kwargs
        # )


class Permission(object):
    """Permission model."""

    def __init__(self, slug, *args, **kwargs):
        """Constructor."""
        self.slug = slugify(slug)
        self.description = kwargs.pop('description', None)
        self.enabled = kwargs.pop('enabled', True)

        # super(Permission, self).__init__(
        #     name=name,
        #     *args, **kwargs
        # )
