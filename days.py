# Question: Write a program in Python to convert a given number of days into days, month, year, and week.

def convert_days(days):
    year = days // 365
    days %= 365
    month = days // 30
    days %= 30
    week = days // 7
    days %= 7
    return year, month, week, days

# Example usage:
days = 400
year, month, week, remaining_days = convert_days(days)
print(f"{days} days is equal to {year} year(s), {month} month(s), {week} week(s), and {remaining_days} day(s)")
