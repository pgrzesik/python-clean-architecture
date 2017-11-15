from rentomatic.shared.response_objects import ResponseFailure


class UseCase(object):

    def execute(self, request_object):
        if not request_object:
            return ResponseFailure.build_from_invalid_request_object(
                request_object)
        return self.process_request(request_object)

    def process_request(self, request_object):
        raise NotImplementedError(
            "process_request() not implemented by UseCase class")
