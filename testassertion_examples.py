import unittest

class TestAllAssertions(unittest.TestCase):

    def test_all_assertions(self):

        # assertEqual
        self.assertEqual(2 + 2, 4)

        # assertNotEqual
        self.assertNotEqual(2 + 2, 5)

        # assertTrue
        self.assertTrue(2 + 2 == 4)

        # assertFalse
        self.assertFalse(2 + 2 == 5)

        # assertIs
        x = [1, 2, 3]
        y = x
        z = [1, 2, 3]
        self.assertIs(x, y)
        self.assertIsNot(x, z)

        # assertIn
        my_list = ['apple', 'banana', 'cherry']
        self.assertIn('apple', my_list)
        self.assertNotIn('orange', my_list)

        # assertIsInstance
        self.assertIsInstance(5, int)
        self.assertNotIsInstance('abc', int)

        # assertAlmostEqual
        self.assertAlmostEqual(0.1 + 0.2 , 0.3, place=7)

        # assertGreater
        self.assertGreater(5, 3)

        # assertGreaterEqual
        self.assertGreaterEqual(5, 5)
        self.assertGreaterEqual(5, 3)

        # assertLess
        self.assertLess(3, 5)

        # assertLessEqual
        self.assertLessEqual(5, 5)
        self.assertLessEqual(3, 5)

        # assertRegex
        self.assertRegex('abc123', r'[a-z]+[0-9]+')
        self.assertNotRegex('abc123', r'[A-Z]+')
        
        # assertCounterEqual
        list1 = [1, 2, 3, 4]
        list2 = [4, 3, 2, 1]
        self.assertCountEqual(list1, list2)

        # assertMultiLineEqual
        str1 = 'Hello\nworld'
        str2 = 'Hello\n     world\n'

        # asserSequenceEqual 
        seq1 = [1, 2, 3]
        seq2 = [1, 2, 3]
        self.assertSequenceEqual(seq1, seq2)

        # assertListEqual
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        self.assertListEqual(list1, list2)


        # assertTupleEqual
        tuple1 = (1, 2, 3)
        tuple2 = (1, 2, 3)
        self.assertTupleEqual(tuple1, tuple2)

        # assertSetEqual
        set1 = {1, 2, 3}
        set2 = {1, 2, 3}
        self.assertSetEqual(set1, set2)

        # assertDictEqual
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 2, 'a': 1}
        self.assertDictEqual(dict1, dict2)



    if __name__ == '__main__':
        unittest.main()