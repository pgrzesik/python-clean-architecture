from unittest import mock

import pytest

from rentomatic.domain.storageroom import StorageRoom
from rentomatic.shared.response_objects import ResponseFailure
from rentomatic.use_cases.request_objects import StorageRoomListRequestObject
from rentomatic.use_cases.storageroom_use_cases import StorageRoomListUseCase


class TestStorageRoomListUseCase:
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

    @pytest.fixture
    def use_case(self, repo_mock):
        return StorageRoomListUseCase(repo_mock)

    def test_use_case(self, domain_storagerooms, repo_mock, use_case):
        req = StorageRoomListRequestObject.from_dict({})
        res = use_case.execute(req)

        repo_mock.list.assert_called_once_with(filters=None)
        assert res.value == domain_storagerooms

    def test_use_case_with_filters(
            self, domain_storagerooms, repo_mock, use_case):
        filters = {'a': 'b'}
        req = StorageRoomListRequestObject.from_dict({'filters': filters})

        res = use_case.execute(req)

        repo_mock.list.assert_called_once_with(filters=filters)
        assert res.value == domain_storagerooms

    def test_use_case_handles_bad_request(self, repo_mock, use_case):
        bad_filters = [1, 2, 3]
        req = StorageRoomListRequestObject.from_dict({'filters': bad_filters})

        res = use_case.execute(req)

        repo_mock.list.assert_not_called
        assert res.value == {
            'type': ResponseFailure.PARAMETERS_ERROR,
            'message': 'filters: is not Mapping'
        }
