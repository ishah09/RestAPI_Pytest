from utilconfig.commonutil import CommonUtil

request_method = "GET"
endpoint = "api/users?page=2"
timeout_A = 1
timeout_B = 0.01

call_util = CommonUtil()


def test_validate_request_timeout_A():
    assert call_util.make_request_call(request_method, endpoint, ptimeout=timeout_A)


def test_validate_request_timeout_B():
    assert call_util.make_request_call(request_method, endpoint, ptimeout=timeout_B)
