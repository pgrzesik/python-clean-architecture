import json

from flask import Blueprint, Response

from rentomatic.repository.memrepo import MemRepo
from rentomatic.serializers.storageroom_serializer import StorageRoomEncoder
from rentomatic.use_cases.request_objects import StorageRoomListRequestObject
from rentomatic.use_cases.storageroom_use_cases import StorageRoomListUseCase

blueprint = Blueprint('storageroom', __name__)


@blueprint.route('/storagerooms', methods=['GET'])
def storageroom():
    request_object = StorageRoomListRequestObject.from_dict({})

    repo = MemRepo()
    use_case = StorageRoomListUseCase(repo)
    response = use_case.execute(request_object)

    return Response(
        json.dumps(
            response.value, cls=StorageRoomEncoder
        ), status=200
    )
