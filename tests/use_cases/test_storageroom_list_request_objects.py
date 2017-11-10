from rentomatic.use_cases.request_objects import StorageRoomListRequestObject


class TestStorageRoomListRequestObject:
    def test_build(self):
        req = StorageRoomListRequestObject()

        assert req.is_valid()
        assert req.filters is None

    def test_build_from_dict(self):
        req = StorageRoomListRequestObject.from_dict({})

        assert req.is_valid()
        assert req.filters is None

    def test_build_with_empty_filters(self):
        req = StorageRoomListRequestObject(filters={})

        assert req.is_valid()
        assert req.filters == {}

    def test_build_from_dict_with_empty_filters(self):
        req = StorageRoomListRequestObject.from_dict({'filters': {}})

        assert req.is_valid()
        assert req.filters == {}

    def test_build_with_filters(self):
        req = StorageRoomListRequestObject(filters={'a': 'b'})

        assert req.is_valid()
        assert req.filters == {'a': 'b'}

    def test_build_from_dict_with_filters(self):
        req = StorageRoomListRequestObject.from_dict(
            {'filters': {'a': 'b'}})

        assert req.is_valid()
        assert req.filters == {'a': 'b'}

    def test_build_from_dict_with_invalid_filters(self):
        req = StorageRoomListRequestObject.from_dict({'filters': 5})

        assert not req.is_valid()
        assert req.has_errors()
        assert req.errors[0]['parameter'] == 'filters'
