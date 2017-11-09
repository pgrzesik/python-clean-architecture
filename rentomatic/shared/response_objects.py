class ResponseSuccess:
    def __init__(self, value=None):
        self.value = value


class ResponseFailure:
    RESOURCE_ERROR = 'ResourceError'
    PARAMETERS_ERROR = 'ParametersError'
    SYSTEM_ERROR = 'SystemError'

    def __init__(self, type_, message):
        self.type = type_
        self.message = message

    @property
    def value(self):
        return {
            'type': self.type,
            'message': self.message
        }

    @classmethod
    def build_from_invalid_request_object(cls, invalid_request_object):
        message = '\n'.join(
            "{}: {}".format(err['parameter'], err['message'])
            for err in invalid_request_object.errors)

        return cls(cls.PARAMETERS_ERROR, message)
