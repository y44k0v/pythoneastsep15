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
        self.assertIsNone(calculate_bmi(70, 0))


    def test_edge_case_negative_height(self):
        # Test what happens if height is negative
        self.assertIsNone(calculate_bmi(70, -1.75))
        

    def test_edge_case_negative_weight(self):
        # Test what happens if weight is negative
        self.assertIsNone(calculate_bmi(-70, 1.75))
        

    def test_large_values(self):
        # Test with very large values to ensure no overflow issues (though unlikely for BMI)
        self.assertAlmostEqual(calculate_bmi(200, 2.5), 32.0, places=2)

    def test_small_values(self):
        # Test with small but valid height/weight
        self.assertAlmostEqual(calculate_bmi(1, 0.5), 4.0, places=2)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)