event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
day = int(input("Enter day: "))



print()
print("Formatted Output: ")
print("Event: ", event_title.upper())

import calendar

try:
    if 1 <= month <= 12:
        full_month = calendar.month_name[month]
        print(f"Date: {full_month} ", day, ",", year)
        
    else: 
        print("Invalid number. Please enter a number between 1 and 12.")
        
except ValueError:
    print("Invalid input. Please enter a whole number.")
    
print("Year: ", year)
print(f"Month: {full_month}")
print("Day: ", day)