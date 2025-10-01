"""
Instructions:

Given two non-empty arrays of integers, write a function that determines whether the second array
is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but
that are in the same order as they appear in the array. For example, the numbers [1, 3, 4] form
a subsequence of the array [1, 2, 3, 4], and so do [2, 4].

You can assume that there will only be one subsequence.

Example:
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
Expected Output: True

Example 2:
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, 10, -1]
Expected Output: False (because -1 comes before 10 in the sequence, but after in the array)
"""


def isValidSubsequence(array, sequence):
    # Write your code here.
    pass

if __name__ == '__main__':
    # Test cases (you can add more here to test your solution)
    print(f"Test 1: array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[1, 6, -1, 10] -> {isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])}")
    print(f"Test 2: array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[1, 6, 10, -1] -> {isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, 10, -1])}")
    print(f"Test 3: array=[1, 2, 3, 4], sequence=[1, 3, 4] -> {isValidSubsequence([1, 2, 3, 4], [1, 3, 4])}")
    print(f"Test 4: array=[1, 2, 3, 4], sequence=[2, 4] -> {isValidSubsequence([1, 2, 3, 4], [2, 4])}")
    print(f"Test 5: array=[1, 2, 3, 4], sequence=[5] -> {isValidSubsequence([1, 2, 3, 4], [5])}")