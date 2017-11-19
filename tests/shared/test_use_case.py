from unittest import mock

import pytest

from rentomatic.shared.request_objects import InvalidRequestObject
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
        assert res.message == (
            'NotImplementedError: process_request()'
            ' not implemented by UseCase class')

    @pytest.fixture
    def invalid_req(self):
        req = InvalidRequestObject()
        req.add_error('param', 'msg')

    def def_can_process_invalid_request(self, invalid_req):
        use_case = UseCase()

        res = use_case.execute(invalid_req)

        assert res.type == ResponseFailure.PARAMETERS_ERROR
        assert res.message == 'param: msg'

    @pytest.fixture
    def use_case_process_request_exc(self):
        use_case = UseCase()

        class TestException(Exception):
            pass

        use_case.process_request = mock.Mock()
        use_case.process_request.side_effect = TestException('msg')

        return use_case

    def test_can_handle_exc_from_process_request(
            self, use_case_process_request_exc, valid_req):
        res = use_case_process_request_exc.execute(valid_req)

        assert res.type == ResponseFailure.SYSTEM_ERROR
        assert res.message == 'TestException: msg'
