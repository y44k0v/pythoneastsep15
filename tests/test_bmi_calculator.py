import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bmi_calculator import calculate_bmi

class TestBMICalculator(unittest.TestCase):

    def test_standard_bmi_values(self):
        # Test with typical valid inputs
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)
        self.assertAlmostEqual(calculate_bmi(90, 1.80), 27.78, places=2)
        self.assertAlmostEqual(calculate_bmi(55, 1.60), 21.48, places=2)

    def test_zero_weight(self):
        # Test with zero weight
        self.assertAlmostEqual(calculate_bmi(0, 1.70), 0.0)

    def test_height_of_one(self):
        # Test where height is exactly 1 meter
        self.assertAlmostEqual(calculate_bmi(60, 1.0), 60.0)

    def test_edge_case_zero_height(self):
        # Test what happens if height is zero
        # Depending on student's implementation, this might return None or raise an error
        # Adjust this test based on what you expect from their 'edge case' handling
        # Example 1: if they return None for invalid height
        self.assertIsNone(calculate_bmi(70, 0))
        # Example 2: if they raise a ValueError
        # with self.assertRaises(ValueError):
        #     calculate_bmi(70, 0)

    def test_edge_case_negative_height(self):
        # Test what happens if height is negative
        # Adjust this test based on what you expect from their 'edge case' handling
        # Example 1: if they return None for invalid height
        self.assertIsNone(calculate_bmi(70, -1.75))
        # Example 2: if they raise a ValueError
        # with self.assertRaises(ValueError):
        #     calculate_bmi(70, -1.75)

    def test_edge_case_negative_weight(self):
        # Test what happens if weight is negative
        # The formula will still work mathematically, but a negative weight is
        # not physically possible, so students might handle this.
        # For simplicity, we might let the formula run, or expect a specific handling.
        # If formula is expected:
        self.assertAlmostEqual(calculate_bmi(-70, 1.75), -22.86, places=2)
        # If specific handling (e.g., returning None or raising error):
        # self.assertIsNone(calculate_bmi(-70, 1.75))
        # with self.assertRaises(ValueError):
        #     calculate_bmi(-70, 1.75)

    def test_large_values(self):
        # Test with very large values to ensure no overflow issues (though unlikely for BMI)
        self.assertAlmostEqual(calculate_bmi(200, 2.5), 32.0, places=2)

    def test_small_values(self):
        # Test with small but valid height/weight
        self.assertAlmostEqual(calculate_bmi(1, 0.5), 4.0, places=2)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)