"""
E2E tests.
"""

from sqlalchemy.inspection import inspect
from cerberusauth.schema import sql as sqlschema

EXPECTED_MODELS = ['user', 'role', 'userrole', 'permission', 'rolepermission']


def test_schema_creation(cerberus_fixture):
    """."""
    assert "sqlite" in str(sqlschema.sqlstorage.engine)
    iengine = inspect(sqlschema.sqlstorage.engine)

    assert set(iengine.get_table_names()) == set(EXPECTED_MODELS)


def test_register_new_user(cerberus_fixture):
    """."""
    new_user_dict = {"email": "geoff@ting.com", "fullname": "Geoff Jeff"}
    new_users = cerberus_fixture.register.register_users(new_user_dict)

    assert new_users
    assert isinstance(new_users, list)

    new_user = new_users[0]

    user = new_user.user
    assert user.email == new_user_dict["email"]
    assert user.fullname == new_user_dict["fullname"]
    assert user.password
    assert isinstance(user.password, bytes)
    assert len(user.password) > 25
    assert user.has_temp_password
    assert user.created
    assert user.modified
