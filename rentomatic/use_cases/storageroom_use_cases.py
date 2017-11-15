from rentomatic.shared.response_objects import ResponseSuccess
from rentomatic.shared.use_case import UseCase


class StorageRoomListUseCase(UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        storageroom = self.repo.list(filters=request_object.filters)
        return ResponseSuccess(storageroom)
