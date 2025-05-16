import unittest

class TestSkip(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_skip(self):
        self.fail("this test should have beenskipped")

    def test_string_upper(self):
        self.assertEqual("hello".upper(), "HELLO")


if __name__ == "__main__":
    unittest.main()