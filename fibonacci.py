def calculate_fibonacci(n):
    """
    Calculates the nth number in the Fibonacci sequence.
    Example:
    calculate_fibonacci(0) -> 0
    calculate_fibonacci(1) -> 1
    calculate_fibonacci(5) -> 5
    """
    if n<0:
        raise ValueError("Negative Integers are not allowed")
    
    if n==0 : return 0
    if n==1 : return 1

    count=2
    previous, current,next=0,1,0
    while count<n+1:
        next=current+previous
        previous=current
        current=next 
        count+=1
    return next