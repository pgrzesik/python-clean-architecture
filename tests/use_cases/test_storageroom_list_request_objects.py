from rentomatic.use_cases import request_objects


def build_storageroom_list_request_object():
    req = request_objects.StorageRoomListRequestObject()

    assert req


def test_build_storageroom_list_request_object_from_dict():
    req = request_objects.StorageRoomListRequestObject.from_dict({})

    assert req
