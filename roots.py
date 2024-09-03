# Question: Write a program in Python to find the roots of a Quadratic equation.

import math

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "Complex Roots"

# Example usage:
a = 1
b = -7
c = 12
roots = find_roots(a, b, c)
print(f"The roots of the quadratic equation are: {roots}")
