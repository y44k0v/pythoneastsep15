def calculate_fibonacci(n):
    """
    Calculates the nth number in the Fibonacci sequence.
    Example:
    calculate_fibonacci(0) -> 0
    calculate_fibonacci(1) -> 1
    calculate_fibonacci(5) -> 5
    """
    # TODO: Student must write their code here.
    # For now, let's provide a placeholder that will fail the test.

    """Return the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)


print("Fibonacci(0) =", calculate_fibonacci(0))
print("Fibonacci(1) =", calculate_fibonacci(1))
print("Fibonacci(5) =", calculate_fibonacci(5))
 