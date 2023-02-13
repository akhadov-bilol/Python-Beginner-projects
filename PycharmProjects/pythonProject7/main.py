
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_value = 0
for score in student_scores:
    if score > max_value:
        max_value = score
print(max_value)



