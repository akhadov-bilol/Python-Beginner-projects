student_heights = input("Input a list of student heights").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int((student_heights[n]))
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)


students_number = 0
for student in student_heights:
    students_number += 1
print(students_number)
average_height = round(total_height / students_number)
print(average_height)

