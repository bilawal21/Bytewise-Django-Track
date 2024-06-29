# Write a Python program to display the calendar of a given month and year.

import calendar

year = int(input("Enter Year: "))
month = int(input("Enter Month: "))

print(calendar.month(year,month))