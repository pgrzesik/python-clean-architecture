from rentomatic.shared.response_objects import ResponseSuccess


class StorageRoomListUseCase:

    def __init__(self, repo):
        self.repo = repo

    def execute(self, req):
        storage_rooms = self.repo.list()
        return ResponseSuccess(value=storage_rooms)
