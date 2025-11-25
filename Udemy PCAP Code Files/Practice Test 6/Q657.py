
# Letter Grade Converter
grade = int(input('Enter a numeric grade:'))
if grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 65:
    letter_grade = 'D'
else:
    letter_grade = 'F'
print('Your letter grade is:', letter_grade)
