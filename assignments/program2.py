# Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

def generate_list_and_tuple():
    input_sequence = input("Enter a sequence of comma-separated numbers: ")
    number_list = input_sequence.split(",")
    number_tuple = tuple(number_list)
    return number_list, number_tuple

# Example usage:
number_list, number_tuple = generate_list_and_tuple()
print(number_list)
print(number_tuple)
