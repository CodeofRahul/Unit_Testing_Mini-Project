from unittest.mock import MagicMock
import unittest

class MyClass:
    def my_method(self):
        return "real"
    
class test_magic_mock(unittest.TestCase):
    # Create a MagicMock object
    my_mock = MagicMock(spec=MyClass)

    # Set a return value for the mock object
    my_mock.my_method.return_value = "mocked"

    # Call the mock object
    result = my_mock.my_method()

    # verify the result
    assert result == "mocked"

if __name__ == '__main__':
    unittest.main()
    