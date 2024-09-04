# Question: Write a Python program to print Fibonacci series of n terms.

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Example usage:
n = int(input("Enter the number of terms: "))
print(f"Fibonacci series of {n} terms: {fibonacci(n)}")
