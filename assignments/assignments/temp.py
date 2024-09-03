# Question: Write a program in Python to convert any temperature from Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius):
    # Conversion formula: F = (C * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage:
celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")
