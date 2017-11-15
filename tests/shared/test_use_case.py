from unittest import mock

import pytest

from rentomatic.shared.response_objects import ResponseFailure
from rentomatic.shared.use_case import UseCase


class TestUseCase:

    @pytest.fixture
    def valid_req(self):
        m = mock.Mock()
        m.is_valid.return_value = True
        return m

    def test_cannot_process_valid_request(self, valid_req):

        use_case = UseCase()

        res = use_case.execute(valid_req)

        assert isinstance(res, ResponseFailure)
        assert res.type == ResponseFailure.SYSTEM_ERROR
        assert res.message == ('NotImplementedError: process_request()'
                               ' not implemented by UseCase class')
