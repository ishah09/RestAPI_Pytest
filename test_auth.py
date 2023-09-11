from utilconfig.commonutil import CommonUtil

request_method = "GET"
endpoint = "https://the-internet.herokuapp.com/basic_auth"

call_util = CommonUtil()

authkey = "admin", "demo"


def test_validate_request_with_authentication():
    assert call_util.make_request_call(request_method, endpoint, auth=authkey)
