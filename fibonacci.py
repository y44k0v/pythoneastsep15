def calculate_fibonacci(n):
    """
    Calculates the nth number in the Fibonacci sequence.
    Example:
    calculate_fibonacci(0) -> 0
    calculate_fibonacci(1) -> 1
    calculate_fibonacci(5) -> 5
    """
    # TODO: Student must write their code here.
    def fibonacci(n):
    if (n==0 or n == 1):
      return n
    elif (n > 1):
       return fibonacci(n - 1) + fibonacci(n - 2)
  
'''def fibonacci_neg(n):
    if (n==(-1) or n==(0)):
       return abs(n)
    elif (n==(-2)):
       return -1
    else:
       return fibonacci_neg(n + 2) - fibonacci_neg(n + 1)
'''

n= int(input("Entrer unnombre"))
if (n >= 0):
  i=0
  while (i <= n-1):
      #print(fibonacci(i), end=",")
      i=i+1
  print("The fibonacci is :",fibonacci(i))
'''if (n < 0):
  i = n
  while (i < -2):
      print((i+2)," i ",(i+1)) 
      i=i+1
      print("f",fibonacci_neg(i))
  #print("fib",i,fibonacci_neg(i))'''
    # For now, let's provide a placeholder that will fail the test.
    return -1
