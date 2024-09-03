# Question: Write a program in Python to print the sum of natural numbers.

def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

# Example usage:
n = int(input("Enter a number: "))
total_sum = sum_of_natural_numbers(n)
print(f"The sum of natural numbers from 1 to {n} is: {total_sum}")
