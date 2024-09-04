# Question: Write a Python program to implement multiplication table.

def multiplication_table(number, upto=10):
    return [number * i for i in range(1, upto + 1)]

# Example usage:
number = int(input("Enter the number: "))
table = multiplication_table(number)
for i, value in enumerate(table, start=1):
    print(f"{number} x {i} = {value}")
