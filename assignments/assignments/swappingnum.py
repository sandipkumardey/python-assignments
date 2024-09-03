# Question: Write a program in Python to swap two numbers without using a third variable.

def swap_numbers(a, b):
    # Swapping using addition and subtraction
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Example usage:
a = 10
b = 20
a, b = swap_numbers(a, b)
print(f"Swapped values: a = {a}, b = {b}")
