# Question: Write a Python program to perform Linear search.

def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

# Example usage:
n = int(input("Enter the number of elements: "))
lst = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
target = int(input("Enter the number to search for: "))
result = linear_search(lst, target)
if result != -1:
    print(f"Number found at index: {result}")
else:
    print("Number not found.")
