import csv
import json
import os

import requests

from utilconfig.configreader import ConfigfileReader


class CommonUtil:
    util_response = ''
    config_utils = ConfigfileReader(os.getcwd())

    def __init__(self):
        self.response = None

    def make_request_call(self, request_type, target_url, **kwargs):
        """
            This is common service call which will request for given service
        :param request_type:
        :param target_url:
        :return:
        """

        try:
            timeout = kwargs.get("ptimeout")
            payload = kwargs.get("json")
            authentication = kwargs.get("auth")

            if "https" in target_url:
                source_url = target_url
            else:
                source_url = self.config_utils.get_baseurl() + target_url

            if request_type == "GET":
                self.response = requests.get(source_url, timeout=timeout, auth=authentication, verify=False)
            elif request_type == "POST":
                self.response = requests.post(source_url, json=payload, timeout=timeout, auth=authentication,
                                              verify=False)
            elif request_type == "PUT":
                self.response = requests.put(source_url, json=payload, timeout=timeout, auth=authentication,
                                             verify=False)
            elif request_type == "PATCH":
                self.response = requests.patch(source_url, json=payload, timeout=timeout, auth=authentication,
                                               verify=False)
            elif request_type == "DELETE":
                self.response = requests.delete(source_url, timeout=timeout, auth=authentication, verify=False)

            util_response = self.response

            return self.check_status_code(util_response, request_type)
        except Exception as e:
            print(str(e))

    def check_status_code(self, response, request_type):
        """
            This method check and validate response status
        :param self:
        :param response:
        :param request_type:
        :return:
        """
        if request_type == 'GET' or request_type == 'PUT' or request_type == 'PATCH' and response.status_code == 200:
            self.get_common_response_details(response)
            return True
        elif request_type == 'POST' and response.status_code == 201 or response.status_code == 200:
            self.get_common_response_details(response)
            return True
        elif request_type == 'DELETE' and response.status_code == 204:
            self.get_common_response_details(response)
            return True
        else:
            return False

    def get_common_response_details(self, response):
        """

        :param get_response:
        :return:
        """
        print("Response Code:", response)
        print("Response Status Code:", response.status_code)
        print("Response Content:", response.content)
        print("Response Header:", response.headers)
        print("Response Time:", response.elapsed)
        print("Text:", response.text)
        # print("JSON:", response.json())

        # json_response = response.json()
        # print("Specific Parameter URL:", json_response['support']['url'])

    def get_key_value(self, pstr_jsonkey):
        """

        :param response:
        :return:
        """
        getvalue = json.loads(self.response.content)[pstr_jsonkey]
        return getvalue

    def check_existance_of_key(self, text):
        """

        :param text:
        :return:
        """
        try:
            flag = False
            json_str = json.dumps(self.response)
            if json_str.find(text) != -1:
                flag = True
            else:
                flag = False
        except Exception as e:
            print(str(e))
            flag = False
        return flag

    # def read_test_data_from_csv(self):
    #     test_data = []
    #     with open("test_data/...csv", newline="") as csvfile:
    #         data = csv.reader(csvfile, delimiter=",")
    #         next(data)  # skip header row
    #         for row in data:
    #             test_data.append(row)
    #     return test_data


