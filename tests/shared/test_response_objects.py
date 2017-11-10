import pytest

from rentomatic.shared.response_objects import ResponseFailure, ResponseSuccess
from rentomatic.use_cases.request_objects import InvalidRequestObject


@pytest.fixture
def response_value():
    return {
        'key': ['value', 'second_value']
    }


@pytest.fixture
def response_type():
    return 'ResponseError'


@pytest.fixture
def response_message():
    return 'This is an error'


class TestResponseSuccess:
    def test_response_success(self, response_value):
        res = ResponseSuccess(response_value)

        assert res.value == response_value


class TestResponseFailure:
    def test_contains_type_and_message(self, response_type, response_message):
        res = ResponseFailure(response_type, response_message)

        assert res.type == response_type
        assert res.message == response_message

    def test_contains_value(self, response_type, response_message):
        res = ResponseFailure(response_type, response_message)

        assert res.value == {
            'type': response_type,
            'message': response_message
        }

    @pytest.fixture
    def invalid_request_object(self):
        req = InvalidRequestObject()
        req.add_error('path', 'Is mandatory')
        req.add_error('path', 'can\'t be blank')
        return req

    def test_build_from_invalid_request_object(self, invalid_request_object):
        res = ResponseFailure.build_from_invalid_request_object(
            invalid_request_object)

        assert res.type == ResponseFailure.PARAMETERS_ERROR
        assert res.message == 'path: Is mandatory\npath: can\'t be blank'

    def test_build_resource_error(self, response_message):
        res = ResponseFailure.build_resource_error(response_message)

        assert res.type == ResponseFailure.RESOURCE_ERROR
        assert res.message == response_message

    def test_build_parameters_error(self, response_message):
        res = ResponseFailure.build_parameters_error(response_message)

        assert res.type == ResponseFailure.PARAMETERS_ERROR
        assert res.message == response_message

    def test_build_system_error(self, response_message):
        res = ResponseFailure.build_system_error(response_message)

        assert res.type == ResponseFailure.SYSTEM_ERROR
        assert res.message == response_message
