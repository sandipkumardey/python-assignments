# Question: Write a Python program to take input from user in a list and print it.

def input_list():
    n = int(input("Enter the number of elements: "))
    lst = [input(f"Enter element {i+1}: ") for i in range(n)]
    return lst

# Example usage:
user_list = input_list()
print("The list you entered is:", user_list)
