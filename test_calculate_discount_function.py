import unittest
import calculate_discount

class test_calculate_discount_function(unittest.TestCase):

    def test_calculate_discount_function_1000(self):
        self.assertEqual(calculate_discount.calculate_discount_function(1000), 50.0)

    def test_calculate_discount_function_5000(self):
        self.assertEqual(calculate_discount.calculate_discount_function(5000), 250.0)
        
    def test_calculate_discount_function_10000(self):
        self.assertEqual(calculate_discount.calculate_discount_function(10000), 1200.0)

    def test_calculate_discount_function_15000(self):
        self.assertEqual(calculate_discount.calculate_discount_function(15000), 1800.0)

    def test_calculate_discount_function_25000(self):
        self.assertEqual(calculate_discount.calculate_discount_function(25000), 7500.0)


if __name__ == '__main__':
    unittest.main()