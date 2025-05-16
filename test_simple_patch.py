from unittest.mock import patch
import unittest

def my_function():
    return "Real value"

class test_simple_patches(unittest.TestCase):

    @patch('__main__.my_function')
    def test_mocked_function(self, mock_function):
        mock_function.return_value = "Mocked value"
        assert my_function() == "Mocked value"

if __name__ == '__main__':
    unittest.main()