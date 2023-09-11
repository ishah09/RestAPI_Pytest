import pytest

from utilconfig.commonutil import CommonUtil

request_method = "GET"
endpoint = "api/users?page=2"

call_util = CommonUtil()


@pytest.fixture
def callutil():
    assert call_util.make_request_call(request_method, endpoint)


def test_validate_with_assertion(callutil):
    assert call_util.get_key_value('total_pages') == 2, "Total Pages should be 2"
    # assert (json_response["data"][0]["email"]).endswith("reqres.in"), "Email should ends with reqres.in"

