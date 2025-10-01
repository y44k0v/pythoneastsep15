"""
Instructions:

You are given a non-empty array of distinct integers and an integer representing a target sum.
Write a function that finds if any two numbers in the array sum up to the target sum.
If they do, return them in an array, otherwise return an empty array.

You can assume that there will be at most one pair of numbers summing up to the target sum.

Example:
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

Expected Output: [-1, 11] (the order of the numbers doesn't matter)
"""

def twoNumberSum(array, targetSum):
    # Write your code here.
    pass

if __name__ == '__main__':
    # Test cases (you can add more here to test your solution)
    print(f"Test 1: [1, 3, 4, 5], targetSum=7 -> {twoNumberSum([1, 3, 4, 5], 7)}")
    print(f"Test 2: [3, 5, -4, 8, 11, 1, -1, 6], targetSum=10 -> {twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)}")
    print(f"Test 3: [4, 6], targetSum=10 -> {twoNumberSum([4, 6], 10)}")
    print(f"Test 4: [4, 6, 1], targetSum=5 -> {twoNumberSum([4, 6, 1], 5)}")
    print(f"Test 5: [1, 2, 3, 4, 5, 6, 7, 8, 9], targetSum=17 -> {twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 17)}")