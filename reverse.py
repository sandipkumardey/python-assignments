# Question: Write a program in Python to print the reverse of a number.

def reverse_number(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10
    return reversed_num

# Example usage:
number = int(input("Enter a number: "))
reversed_num = reverse_number(number)
print(f"The reverse of {number} is: {reversed_num}")
