# Question: Write a Python program to find Factorial of a given number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
n = int(input("Enter a number: "))
print(f"The factorial of {n} is {factorial(n)}.")
