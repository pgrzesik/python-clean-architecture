import uuid

from rentomatic.domain.storageroom import StorageRoom


def test_storageroom_model_init():
    code = uuid.uuid4()
    storageroom = StorageRoom(
        code, size=200, price=100, longitude='-0.099123', latitude='51.7543')

    assert storageroom.code == code
    assert storageroom.size == 200
    assert storageroom.price == 100
    assert storageroom.longitude == -0.099123
    assert storageroom.latitude == 51.7543


def test_storagemodel_from_dict():
    code = uuid.uuid4()
    storageroom = StorageRoom.from_dict(
        {
            'code': code,
            'size': 200,
            'price': 100,
            'longitude': '-0.099123',
            'latitude': '51.7543'
        })

    assert storageroom.code == code
    assert storageroom.size == 200
    assert storageroom.price == 100
    assert storageroom.longitude == -0.099123
    assert storageroom.latitude == 51.7543
