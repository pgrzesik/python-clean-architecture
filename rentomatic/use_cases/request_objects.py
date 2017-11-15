import collections

from rentomatic.shared.request_objects import (
    InvalidRequestObject, ValidRequestObject)


class StorageRoomListRequestObject(ValidRequestObject):

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, params):
        invalid_req = InvalidRequestObject()

        if 'filters' in params and \
           not isinstance(params['filters'], collections.Mapping):
            invalid_req.add_error('filters', 'is not Mapping')

        if invalid_req.has_errors():
            return invalid_req

        return StorageRoomListRequestObject(**params)
