class BaseRequestObject:
    def is_valid(self):
        raise NotImplemented


class InvalidRequestObject:
    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({'parameter': parameter, 'message': message})

    def has_errors(self):
        return len(self.errors) > 0

    def is_valid(self):
        return False


class ValidRequestObject:
    @classmethod
    def from_dict(cls, params):
        raise NotImplemented

    def is_valid(self):
        return True
