import pytest

from utilconfig.commonutil import CommonUtil

request_method = "GET"
endpoint = "api/users?page=2"

call_util = CommonUtil()


@pytest.mark.basic
def test_validate_request_success():
    assert call_util.make_request_call(request_method, endpoint)
