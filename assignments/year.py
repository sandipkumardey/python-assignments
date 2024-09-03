# Question: Write a program in Python to check a given year is leap year or not.

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage:
year = int(input("Enter a year: "))
is_leap_year = check_leap_year(year)
if is_leap_year:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
