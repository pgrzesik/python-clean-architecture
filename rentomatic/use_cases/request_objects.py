class StorageRoomListRequestObject:

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, params):
        return StorageRoomListRequestObject(**params)
