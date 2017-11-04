import json

from rentomatic.domain.storageroom import StorageRoom
from rentomatic.serializers import storageroom_serializer


def test_serialize_domain_storageroom():
    room = StorageRoom(
        'some_uuid',
        size=200,
        price=10,
        longitude='-0.09123',
        latitude='51.761234')

    expected_json = '''
        {
            "code": "some_uuid",
            "size": 200,
            "price": 10,
            "longitude": -0.09123,
            "latitude": 51.761234
        }
    '''

    result = json.dumps(room, cls=storageroom_serializer.StorageRoomEncoder)

    assert json.loads(result) == json.loads(expected_json)
