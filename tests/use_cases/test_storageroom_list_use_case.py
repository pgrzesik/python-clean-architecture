from unittest import mock

import pytest

from rentomatic.domain.storageroom import StorageRoom
from rentomatic.use_cases.request_objects import StorageRoomListRequestObject
from rentomatic.use_cases.storageroom_use_cases import StorageRoomListUseCase


class TestStorageRoom:
    @pytest.fixture
    def domain_storagerooms(self):
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
    def repo_mock(self, domain_storagerooms):
        m = mock.Mock()
        m.list.return_value = domain_storagerooms
        return m

    def test_list(self, domain_storagerooms, repo_mock):
        storageroom_list_use_case = StorageRoomListUseCase(repo_mock)
        req = StorageRoomListRequestObject.from_dict({})
        res = storageroom_list_use_case.execute(req)

        repo_mock.list.assert_called_once_with(filters=None)
        assert res.value == domain_storagerooms

    def test_list_with_filters(self, domain_storagerooms, repo_mock):
        storageroom_list_use_case = StorageRoomListUseCase(repo_mock)
        filters = {'a': 'b'}
        req = StorageRoomListRequestObject.from_dict({'filters': filters})

        res = storageroom_list_use_case.execute(req)

        repo_mock.list.assert_called_once_with(filters=filters)
        assert res.value == domain_storagerooms
