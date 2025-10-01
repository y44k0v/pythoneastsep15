"""
Instructions:

Write a function that takes in a non-empty array of integers that are sorted in ascending order
and returns a new array of the same length with the squares of the original integers also
sorted in ascending order.

Example:
array = [1, 2, 3, 5, 6, 8, 9]
Expected Output: [1, 4, 9, 25, 36, 64, 81]

Example with negative numbers:
array = [-2, -1, 0, 1, 2]
Expected Output: [0, 1, 1, 4, 4]
"""

def sortedSquaredArray(array):
    # Write your code here.
    pass

if __name__ == '__main__':
    # Test cases (you can add more here to test your solution)
    print(f"Test 1: [1, 2, 3, 5, 6, 8, 9] -> {sortedSquaredArray([1, 2, 3, 5, 6, 8, 9])}")
    print(f"Test 2: [-2, -1, 0, 1, 2] -> {sortedSquaredArray([-2, -1, 0, 1, 2])}")
    print(f"Test 3: [-5, -4, -3, -2, -1] -> {sortedSquaredArray([-5, -4, -3, -2, -1])}")
    print(f"Test 4: [0, 0, 0] -> {sortedSquaredArray([0, 0, 0])}")
    print(f"Test 5: [7, 8, 9, 10] -> {sortedSquaredArray([7, 8, 9, 10])}")