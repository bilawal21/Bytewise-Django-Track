# Write a Python program to print the Fibonacci sequence up to a specified number of terms.


def fibonacci_seq(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci_seq(n-1) + fibonacci_seq(n-2) 


n = int(input("Enter a number: "))

print(f"Fibonacci Sequence of {n} is {fibonacci_seq(n)}")