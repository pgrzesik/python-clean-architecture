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
