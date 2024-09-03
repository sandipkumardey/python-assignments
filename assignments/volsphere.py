# Question: Write a program in Python to find the volume of a sphere with radius 6cm.

import math

def sphere_volume(radius):
    # Volume of a sphere formula: (4/3) * π * r^3
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

# Example usage:
radius = 6
volume = sphere_volume(radius)
print(f"Volume of the sphere with radius {radius}cm: {volume} cubic cm")
