# Question: Take marks of a student of four different subjects, find the average, 
# and depending on the average find Grade (>=75 i.e., ‘A’, >=60 but <=75 i.e., ‘B’, 
# >=40 but <=60 i.e., ‘C’, <=40 i.e., ‘D’).

def calculate_grade(marks):
    average = sum(marks) / len(marks)
    if average >= 75:
        grade = 'A'
    elif average >= 60:
        grade = 'B'
    elif average >= 40:
        grade = 'C'
    else:
        grade = 'D'
    return average, grade

# Example usage:
marks = [int(input(f"Enter marks for subject {i+1}: ")) for i in range(4)]
average, grade = calculate_grade(marks)
print(f"Average: {average}, Grade: {grade}")
