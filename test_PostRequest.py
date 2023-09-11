import pytest

from utilconfig.commonutil import CommonUtil

request_method = "POST"
endpoint = "api/users"
payload = {
    "name": "RestAPI",
    "job": "API Testing"
}

call_util = CommonUtil()


def test_validate_postrequest():
    assert call_util.make_request_call(request_method, endpoint, json=payload)
    print("Job is:", call_util.get_key_value('job'))
