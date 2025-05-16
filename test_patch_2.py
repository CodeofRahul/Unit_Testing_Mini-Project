from unittest.mock import patch
import unittest

class MyClass:
    my_attribute = "Real value"

class test_simple_patch_2(unittest.TestCase):

    @patch('__main__.MyClass.my_attribute', "Mocked value")
    def test_mocked_attribute(self):
        assert MyClass.my_attribute == "Mocked value"

if __name__ == '__main__':
    unittest.main()