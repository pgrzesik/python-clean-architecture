import pytest

from rentomatic.shared.response_objects import ResponseFailure, ResponseSuccess


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
    return 'This is a response error'


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
