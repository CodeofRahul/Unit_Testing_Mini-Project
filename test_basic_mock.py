import unittest
from unittest.mock import Mock
class simple_mock(unittest.TestCase):
    def test_verify_simple_mock(self):

        # Create a mock object
        my_mock = Mock()

        # Set a return value for the mock object
        # my_mock.return_value = 56
        my_mock.return_value = 12

        # call the mock object
        result = my_mock()

        # verify the result
        # assert result == 56
        assert result == 12

if __name__ == '__main__':
    unittest.main()
