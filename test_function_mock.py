import unittest

def my_function():
    return "Real value"

class test_simple_mock_2(unittest.TestCase):

    def test_mocked_function(self):
        # original_function = my_function
        my_function = lambda: "Mocked value"
        result = my_function()
        assert result == "Mocked value"
        # assert original_function() == "Real value"

if __name__ == '__main__':
    unittest.main()
    