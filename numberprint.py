# Question: Write a program in Python to print 1 to n.

def print_numbers(n):
    for i in range(1, n+1):
        print(i, end=" ")

# Example usage:
n = int(input("Enter a number: "))
print_numbers(n)
