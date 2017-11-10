from unittest import mock

import pytest

from rentomatic.domain.storageroom import StorageRoom
from rentomatic.use_cases.request_objects import StorageRoomListRequestObject
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


@pytest.fixture
def repo_mock(domain_storagerooms):
    m = mock.Mock()
    m.list.return_value = domain_storagerooms
    return m


def test_storageroom_list(domain_storagerooms, repo_mock):
    storageroom_list_use_case = StorageRoomListUseCase(repo_mock)
    req = StorageRoomListRequestObject.from_dict({})
    res = storageroom_list_use_case.execute(req)

    repo_mock.list.assert_called_once_with(filters=None)
    assert res.value == domain_storagerooms
