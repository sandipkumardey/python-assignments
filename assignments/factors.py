# Question: Write a program in Python to print factors of a number.

def print_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

# Example usage:
number = int(input("Enter a number: "))
factors = print_factors(number)
print(f"Factors of {number} are: {factors}")
