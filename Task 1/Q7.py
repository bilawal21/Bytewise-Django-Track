# Write a Python program to find the factorial of a number input by the user.


num = int(input("Enter a number to find its factorial: "))

for i in range(1,num):
    num = num * i
print(num)