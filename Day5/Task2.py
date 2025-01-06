student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

sum = 0
for score in student_scores:
    if score > sum:
        sum = score
print(sum)

exam_scores = [8 ,65, 89, 86, 55, 91, 64, 89]
max = 0
for i in exam_scores:
    if i > max:
        max = i
print(max)
