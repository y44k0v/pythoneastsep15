import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from two_number_sum import twoNumberSum

class TestTwoNumberSum(unittest.TestCase):

    def test_example_case(self):
        array = [3, 5, -4, 8, 11, 1, -1, 6]
        targetSum = 10
        expected = [-1, 11]
        result = twoNumberSum(array, targetSum)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)
        self.assertIn(expected[0], result)
        self.assertIn(expected[1], result)

    def test_no_match(self):
        array = [1, 2, 3, 4, 5]
        targetSum = 10
        self.assertEqual(twoNumberSum(array, targetSum), [])

    def test_empty_array(self):
        array = []
        targetSum = 10
        self.assertEqual(twoNumberSum(array, targetSum), [])

    def test_two_elements_match(self):
        array = [4, 6]
        targetSum = 10
        expected = [4, 6]
        result = twoNumberSum(array, targetSum)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)
        self.assertIn(expected[0], result)
        self.assertIn(expected[1], result)

    def test_two_elements_no_match(self):
        array = [4, 7]
        targetSum = 10
        self.assertEqual(twoNumberSum(array, targetSum), [])

    # def test_negative_numbers(self):
    #     array = [-2, -1, 0, 1, 2, 3, 4, 5]
    #     targetSum = 0
    #     expected = [-2, 2]
    #     result = twoNumberSum(array, targetSum)
    #     self.assertIsNotNone(result)
    #     self.assertEqual(len(result), 2)
    #     self.assertIn(expected[0], result)
    #     self.assertIn(expected[1], result)

    def test_target_zero(self):
        array = [-5, 5]
        targetSum = 0
        expected = [-5, 5]
        result = twoNumberSum(array, targetSum)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)
        self.assertIn(expected[0], result)
        self.assertIn(expected[1], result)

    def test_large_numbers(self):
        array = [100, 200, 300, 400]
        targetSum = 700
        expected = [300, 400]
        result = twoNumberSum(array, targetSum)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)
        self.assertIn(expected[0], result)
        self.assertIn(expected[1], result)

    def test_single_element_array(self):
        array = [10]
        targetSum = 10
        self.assertEqual(twoNumberSum(array, targetSum), [])

    def test_multiple_pairs_but_only_one_valid(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        targetSum = 17
        expected = [8, 9]
        result = twoNumberSum(array, targetSum)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)
        self.assertIn(expected[0], result)
        self.assertIn(expected[1], result)

if __name__ == '__main__':
    unittest.main()