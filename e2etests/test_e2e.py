"""
E2E tests.
"""

from sqlalchemy.inspection import inspect
from cerberusauth.schema import sql as sqlschema

EXPECTED_MODELS = ['user', 'role', 'permission']


def test_schema_creation(cerberus_fixture):
    """."""
    assert "sqlite" in str(sqlschema.sqlstorage.engine)
    iengine = inspect(sqlschema.sqlstorage.engine)

    assert set(iengine.get_table_names()) == set(EXPECTED_MODELS)


def test_register_new_user(cerberus_fixture):
    """."""
    new_user_dict = {"email": "geoff@ting.com", "fullname": "Geoff Jeff"}
    new_users = cerberus_fixture.registration.register_users(new_user_dict)

    assert new_users
    assert isinstance(new_users, list)

    new_user = new_users[0]

    assert new_user.email == new_user_dict["email"]
    assert new_user.fullname == new_user_dict["fullname"]
    assert new_user.password
    assert isinstance(new_user.password, bytes)
    assert len(new_user.password) > 25
    assert new_user.has_temp_password
    assert new_user.created
    assert new_user.modified
