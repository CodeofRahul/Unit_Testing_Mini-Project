from unittest.mock import patch
import requests
import unittest

def a_function_with_external_service_call():
    response = requests.get('https://google.com')
    # print(response.text)

    if (response.text.__contains__('<title>Google</title>')):
        return "Valid User"
    else:
        return "Invalid User"
    
class test_mock_scenario(unittest.TestCase):
    def test_mock(self):
        # print('my_function', my_function())
        # use patch to create mock object for requests.get
        mock_get.return_value.text = '<title>Mock Response</title>'

        # call my_function
        result = a_function_with_external_service_call()

        # check the result
        assert result == "Invalid User"

if __name__ == '__main__':
    unittest.main()
    