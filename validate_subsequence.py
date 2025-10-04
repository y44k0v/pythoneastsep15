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
    #Check if either of the array is empty 
    if len(array)==0 or len(sequence)==0:
        return False
    #If given sequence has length more than the available array 
    if len(sequence)>len(array):
         return False
    
    #left pointer for array and right pointer for sequence 
    left, right=0,0

    while left<len(array) and right<len(sequence):
            
            #if element in array also found in sequence then incrment both pointer
            if(array[left]==sequence[right] ):
                 left+=1
                 right+=1
            #Otherwise increment pointer only in array     
            else:
                 left+=1

    #at this point we iterate over all the array element and if we check for the pointer of sequence 
    #if it is smaller than the length of the sequence that means all the elements of sequence are not 
    # encountered hence return false 
    if right<len(sequence):
         return False

    #on the other hand if both array and sequence pointer are having same value that means all the elements 
    #in seuence are encountered hence return True 
    if  right==len(sequence):
         return True



# if __name__ == '__main__':
#     # Test cases (you can add more here to test your solution)
#     print(f"Test 1: array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[1, 6, -1, 10] -> {isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])}")
#     print(f"Test 2: array=[5, 1, 22, 25, 6, -1, 8, 10], sequence=[1, 6, 10, -1] -> {isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, 10, -1])}")
#     print(f"Test 3: array=[1, 2, 3, 4], sequence=[1, 3, 4] -> {isValidSubsequence([1, 2, 3, 4], [1, 3, 4])}")
#     print(f"Test 4: array=[1, 2, 3, 4], sequence=[2, 4] -> {isValidSubsequence([1, 2, 3, 4], [2, 4])}")
#     print(f"Test 5: array=[1, 2, 3, 4], sequence=[5] -> {isValidSubsequence([1, 2, 3, 4], [5])}")