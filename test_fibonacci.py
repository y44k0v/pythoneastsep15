import unittest
from fibonacci import calculate_fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_for_zero(self):
        self.assertEqual(calculate_fibonacci(0), 0)

    def test_fibonacci_for_one(self):
        self.assertEqual(calculate_fibonacci(1), 1)
    
    def test_fibonacci_for_five(self):
        self.assertEqual(calculate_fibonacci(5), 5)

    def test_fibonacci_for_ten(self):
        self.assertEqual(calculate_fibonacci(10), 55)

    def test_fibonacci_with_negative_number(self):
        with self.assertRaises(ValueError):
            calculate_fibonacci(-1)

if __name__ == '__main__':
    unittest.main()
