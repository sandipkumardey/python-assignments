# Question: Write a Python program to find the largest element in the list.

def find_largest(lst):
    return max(lst)

# Example usage:
n = int(input("Enter the number of elements: "))
lst = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
largest = find_largest(lst)
print(f"The largest element in the list is: {largest}")
