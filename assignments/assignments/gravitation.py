# Question: Write a Python Program to find the gravitational force acting between two objects.
# Formula: F = G * (m1 * m2) / d^2

def gravitational_force(m1, m2, distance):
    # Gravitational constant (in N*(m^2)/kg^2)
    G = 6.67430e-11
    # Gravitational force formula: F = G * (m1 * m2) / d^2
    force = G * (m1 * m2) / (distance ** 2)
    return force

# Example usage:
m1 = 5.972e24  # mass of the Earth in kg
m2 = 7.348e22  # mass of the Moon in kg
distance = 384400000  # distance between Earth and Moon in meters
force = gravitational_force(m1, m2, distance)
print(f"Gravitational force between the objects: {force} N")
