from unittest import mock

import pytest

from rentomatic.domain.storageroom import StorageRoom
from rentomatic.use_cases.storageroom_use_cases import StorageRoomListUseCase


@pytest.fixture
def domain_storagerooms():
    first_storageroom = StorageRoom(
        code='123',
        size=100,
        price=10,
        longitude='-0.0911111',
        latitude='51.751111')

    second_storageroom = StorageRoom(
        code='456',
        size=150,
        price=20,
        longitude='-0922222',
        latitude='51.75222')

    return [first_storageroom, second_storageroom]


def test_storageroom_list(domain_storagerooms):
    repo = mock.Mock()
    repo.list.return_value = domain_storagerooms

    storageroom_list_use_case = StorageRoomListUseCase(repo)
    result = storageroom_list_use_case.execute()

    repo.list.assert_called_once_with()
    assert result == domain_storagerooms
