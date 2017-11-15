from rentomatic.shared.response_objects import ResponseFailure


class UseCase(object):

    def execute(self, req):
        if not req.is_valid():
            return ResponseFailure.build_from_invalid_request_object(req)
        try:
            return self.process_request(req)
        except Exception as exc:
            return ResponseFailure.build_system_error(
                '{}: {}'.format(exc.__class__.__name__, exc))

    def process_request(self, request_object):
        raise NotImplementedError(
            "process_request() not implemented by UseCase class")
