from utilconfig.commonutil import CommonUtil

request_method = "PUT"
endpoint = "api/users/2"
payload = {
    "name": "Ishita",
    "job": "zion resident"
}

call_util = CommonUtil()

def test_validate_putrequest():
    assert call_util.make_request_call(request_method, endpoint, json=payload)
