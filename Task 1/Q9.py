# Write a Python program to find all Armstrong numbers within a specified range.


num = int(input("Enter a number: "))

n_digits = len(str(num))

sum = 0

temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** n_digits
    temp //= 10


if num == sum:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")