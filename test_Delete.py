from utilconfig.commonutil import CommonUtil

request_method = "DELETE"
endpoint = "api/users/2"

call_util = CommonUtil()


def test_validate_delete_request():
    assert call_util.make_request_call(request_method, endpoint)
    # assert response.status_code == 204, "User Deletion Success"
