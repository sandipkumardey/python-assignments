# Question: Take input from user if it is greater than 15 print two times of difference 
# if it’s less than 15 print four times of difference.

def calculate_difference(value):
    difference = abs(value - 15)
    if value > 15:
        return 2 * difference
    else:
        return 4 * difference

# Example usage:
value = int(input("Enter a number: "))
result = calculate_difference(value)
print(f"Result: {result}")
