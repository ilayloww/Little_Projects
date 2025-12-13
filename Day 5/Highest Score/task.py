student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_num  = 0

for index in student_scores:
    if max_num < index:
        max_num = index

print(max_num)