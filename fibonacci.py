def calculate_fibonacci(n):
    """
    Calculates the nth number in the Fibonacci sequence.
    Example:
    calculate_fibonacci(0) -> 0
    calculate_fibonacci(1) -> 1
    calculate_fibonacci(5) -> 5
    """
    # Handle negative input
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    # Base cases for the recursion
    elif n == 0:
        return 0
    elif n == 1:
        return 2
    # Recursive step: sum of the two preceding Fibonacci numbers
    else:
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)