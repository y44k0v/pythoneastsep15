import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sorted_square_array import sortedSquaredArray

class TestSortedSquaredArray(unittest.TestCase):

    def test_positive_numbers(self):
        array = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        self.assertEqual(sortedSquaredArray(array), expected)

    def test_negative_and_positive_numbers(self):
        array = [-2, -1, 0, 1, 2]
        expected = [0, 1, 1, 4, 4]
        self.assertEqual(sortedSquaredArray(array), expected)

    def test_all_negative_numbers(self):
        array = [-5, -4, -3, -2, -1]
        expected = [1, 4, 9, 16, 25]
        self.assertEqual(sortedSquaredArray(array), expected)

    def test_single_element(self):
        array = [7]
        expected = [49]
        self.assertEqual(sortedSquaredArray(array), expected)

    def test_single_negative_element(self):
        array = [-7]
        expected = [49]
        self.assertEqual(sortedSquaredArray(array), expected)

    def test_array_with_zeros(self):
        array = [0, 0, 0]
        expected = [0, 0, 0]
        self.assertEqual(sortedSquaredArray(array), expected)

    def test_mixed_array_with_zero(self):
        array = [-3, -1, 0, 2, 4]
        expected = [0, 1, 4, 9, 16]
        self.assertEqual(sortedSquaredArray(array), expected)

    def test_long_array(self):
        array = [-10, -5, 0, 5, 10, 15, 20]
        expected = [0, 25, 25, 100, 100, 225, 400]
        self.assertEqual(sortedSquaredArray(array), expected)

    def test_two_elements_different_signs(self):
        array = [-2, 5]
        expected = [4, 25]
        self.assertEqual(sortedSquaredArray(array), expected)
    
    def test_two_elements_same_sign(self):
        array = [3, 7]
        expected = [9, 49]
        self.assertEqual(sortedSquaredArray(array), expected)

if __name__ == '__main__':
    unittest.main()