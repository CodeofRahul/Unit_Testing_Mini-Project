import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        print("setUp called")

    def tearDown(self):
        del self.data
        print("tearDown called")

    def test_sum(self):
        self.assertEqual(sum(self.data), 15)

    def test_pop(self):
        self.assertEqual(self.data.pop(), 5)
        self.assertEqual(len(self.data), 4)


if __name__ == '__main__':
    unittest.main()