from rentomatic.shared.response_objects import ResponseFailure, ResponseSuccess


class StorageRoomListUseCase:

    def __init__(self, repo):
        self.repo = repo

    def execute(self, req):
        if not req.is_valid():
            return ResponseFailure.build_from_invalid_request_object(req)

        storage_rooms = self.repo.list(filters=req.filters)
        return ResponseSuccess(value=storage_rooms)
