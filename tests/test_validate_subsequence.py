import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from validate_subsequence import isValidSubsequence

class TestIsValidSubsequence(unittest.TestCase):

    def test_example_case_true(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(isValidSubsequence(array, sequence))

    def test_example_case_false(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, 10, -1] # Order is wrong
        self.assertFalse(isValidSubsequence(array, sequence))

    def test_full_subsequence(self):
        array = [1, 2, 3, 4, 5]
        sequence = [1, 2, 3, 4, 5]
        self.assertTrue(isValidSubsequence(array, sequence))

    def test_empty_sequence(self):
        array = [1, 2, 3]
        sequence = []
        self.assertFalse(isValidSubsequence(array, sequence))

    def test_sequence_longer_than_array(self):
        array = [1, 2]
        sequence = [1, 2, 3]
        self.assertFalse(isValidSubsequence(array, sequence))

    def test_non_existent_elements(self):
        array = [1, 2, 3, 4]
        sequence = [1, 5]
        self.assertFalse(isValidSubsequence(array, sequence))

    def test_single_element_true(self):
        array = [1, 2, 3]
        sequence = [2]
        self.assertTrue(isValidSubsequence(array, sequence))

    def test_single_element_false(self):
        array = [1, 2, 3]
        sequence = [4]
        self.assertFalse(isValidSubsequence(array, sequence))

    def test_repeated_elements(self):
        array = [1, 1, 1, 1, 1]
        sequence = [1, 1, 1]
        self.assertTrue(isValidSubsequence(array, sequence))
    
    def test_interspersed_elements(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sequence = [2, 4, 6, 8, 10]
        self.assertTrue(isValidSubsequence(array, sequence))

    def test_subsequence_at_end(self):
        array = [1, 2, 3, 4, 5]
        sequence = [4, 5]
        self.assertTrue(isValidSubsequence(array, sequence))

    def test_subsequence_at_beginning(self):
        array = [1, 2, 3, 4, 5]
        sequence = [1, 2]
        self.assertTrue(isValidSubsequence(array, sequence))

if __name__ == '__main__':
    unittest.main()