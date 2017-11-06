from rentomatic.shared import response_objects


def test_response_success():
    res = response_objects.ResponseSuccess()
    assert res
