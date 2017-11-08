from rentomatic.use_cases import request_objects


def build_storageroom_list_request_object():
    req = request_objects.StorageRoomListRequestObject()

    assert req
    assert req.filters is None


def test_build_storageroom_list_request_object_from_dict():
    req = request_objects.StorageRoomListRequestObject.from_dict({})

    assert req
    assert req.filters is None


def test_build_storageroom_list_request_object_with_empty_filters():
    req = request_objects.StorageRoomListRequestObject(filters={})

    assert req
    assert req.filters == {}
