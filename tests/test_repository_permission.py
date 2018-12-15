"""Tests for PermissionRepository."""

from cerberusauth.repository import permission
from cerberusauth.repository.adapter import sql


def test_permission_repository_factory():
    """."""
    repo = permission.get_repository()

    assert repo
    assert isinstance(repo, permission.PermissionRepository)
    assert isinstance(repo.adapter, sql.SQLRepositoryAdapter)
