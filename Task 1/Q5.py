# Write a Python program to check if a given year is a leap year.


yy = int(input("Enter Year: "))

if(yy % 400 == 0) and (yy % 100 == 0):
    print(f"{yy} is a leap year")

elif(yy % 4 == 0) and (yy % 100 != 0):
    print(f"{yy} is a leap year")

else:
    print(f"{yy} is not a leap year")
