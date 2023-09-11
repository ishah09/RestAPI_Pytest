# import requests
#
# url = "https://reqres.in/api/users"
# payload = {
#     "name": "Ishita",
#     "job": "Shah"
# }
#
# response = requests.post(url, data=payload, timeout=1, verify=False)
#
# print("Response Code:", response)
# print("Response Status Code:", response.status_code)
#
# response = requests.post(url, data=payload, timeout=0.1, verify=False)
#
# print("Response Code:", response)
# print("New Response Status Code:", response.status_code)
import pytest

from utilconfig.commonutil import CommonUtil

request_method = "POST"
endpoint = "api/users"
payload = {
    "name": "RestAPI",
    "job": "API Testing"
}

timeout_A = 1
timeout_B = 0.01

call_util = CommonUtil()


@pytest.fixture
def fix_demo():
    print("\nthis is before fixture demo")
    yield
    print("\nthis is after fixture demo")


def test_validate_postrequest_timeout_A(fix_demo):
    assert call_util.make_request_call(request_method, endpoint, ptimeout=timeout_A)


def test_validate_postrequest_timeout_B(fix_demo):
    assert call_util.make_request_call(request_method, endpoint, ptimeout=timeout_B)
