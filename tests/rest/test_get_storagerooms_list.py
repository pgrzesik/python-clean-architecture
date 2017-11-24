import json
from unittest import mock

import pytest

from rentomatic.domain.storageroom import StorageRoom
from rentomatic.shared.response_objects import ResponseSuccess


@pytest.fixture
def storageroom_dict():
    return {
        'code': '3251a5bd-86be-428d-8ae9-6e51a8048c33',
        'size': 200,
        'price': 10,
        'longitude': -0.09998975,
        'latitude': 51.75436293
    }


@pytest.fixture
def storageroom_model(storageroom_dict):
    return StorageRoom.from_dict(storageroom_dict)


@pytest.fixture
def storagerooms(storageroom_model):
    return [storageroom_model]


@mock.patch(
    'rentomatic.use_cases.storageroom_use_cases.StorageRoomListUseCase')
def test_get(mock_use_case, client, storagerooms, storageroom_dict):
    mock_use_case().execute.return_value = ResponseSuccess(storagerooms)

    http_response = client.get('/storagerooms')

    assert json.loads(http_response.data.decode('UTF-8')) == [storageroom_dict]
    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'
