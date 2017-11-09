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


def test_response_success(response_value):
    res = ResponseSuccess(response_value)

    assert res.value == response_value


def test_response_failure(response_type, response_message):
    res = ResponseFailure(response_type, response_message)

    assert res.type == response_type
    assert res.message == response_message
