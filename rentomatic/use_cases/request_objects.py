import collections


class InvalidRequestObject:

    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({'parameter': parameter, 'message': message})

    def has_errors(self):
        return len(self.errors) > 0


class ValidRequestObject:

    @classmethod
    def from_dict(cls, params):
        raise NotImplemented


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
