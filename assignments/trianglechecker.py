# Question: Write a program in Python to check a triangle is equilateral, scalene or isosceles.

def check_triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "Isosceles"
    else:
        return "Scalene"

# Example usage:
side1 = int(input("Enter first side: "))
side2 = int(input("Enter second side: "))
side3 = int(input("Enter third side: "))
triangle_type = check_triangle_type(side1, side2, side3)
print(f"The triangle is {triangle_type}.")
