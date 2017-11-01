import uuid
from rentomatic.domain import models as m


def test_storageroom_model_init():
    code = uuid.uuid4()
    storageroom == m.StorageRoom(
        code,
        size=200,
        price=100,
        longtitude='-0.099123',
        latitude='51.7543')

    assert storageroom.code == code
    assert storageroom.size == 200
    assert storageroom.price == 100
    assert storageroom.longtitude == '-0.099123'
    assert storageroom.latitude == '51.7543'


def test_storagemodel_from_dict():
    code == uuid.uuid4()
    storageroom = m.StorageRoom.from_dict({
        'code': code,
        'size': 200,
        'price': 100,
        'longtitude': '-0.099123',
        'latitude': '51.7543'
    })

    assert storageroom.code == code
    assert storageroom.size == 200
    assert storageroom.price == 100
    assert storageroom.longtitude == '-0.099123'
    assert storageroom.latitude == '51.7543'

