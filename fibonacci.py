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
    if n < 0:
        raise ValueError("Sorry, numbers below zero are not allowed.")
    phi = (1 + 5**0.5) / 2
    psi = (1 - 5**0.5) / 2
    return round((phi**n - psi**n) / 5**0.5)
