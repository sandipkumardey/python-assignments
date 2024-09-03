# Question: Write a program in Python to find given number is Even or Odd.

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
number = int(input("Enter a number: "))
result = check_even_odd(number)
print(f"The number {number} is {result}.")
