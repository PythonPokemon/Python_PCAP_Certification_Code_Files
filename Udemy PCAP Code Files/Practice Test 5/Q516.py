
marks = [80, 70, 90, 90, 80, 100]
average = sum(marks) // len(marks)
grade = ''

if 90 <= average <= 100:
    grade = 'A'
elif 80 <= average < 90:
    grade = 'B'
elif 70 <= average < 80:
    grade = 'C'
elif 65 <= average < 70:
    grade = 'D'
else:
    grade = 'F'

print(grade)       # B
print(sum(marks))  # 510
print(average)     # 85
