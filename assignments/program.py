# Question: Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

def capitalize_lines():
    lines = []
    print("Enter lines of text (press Enter twice to end):")
    while True:
        line = input()
        if line:
            lines.append(line.upper())
        else:
            break
    for line in lines:
        print(line)