from utilconfig.commonutil import CommonUtil

request_method = "POST"
endpoint = "api/register"
payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

call_util = CommonUtil()


def test_validate_postrequest():
    assert call_util.make_request_call(request_method, endpoint, json=payload)
    print("Get Value of Token:", call_util.get_key_value('token'))
