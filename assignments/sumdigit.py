# Question: Write a program in Python to print the sum of digits.

def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

# Example usage:
number = int(input("Enter a number: "))
sum_digits = sum_of_digits(number)
print(f"The sum of digits of {number} is: {sum_digits}")
