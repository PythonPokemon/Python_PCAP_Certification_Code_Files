
# ABC Video, DVD Rental Calculator

# ontime = input('Was the video returned before 8pm? y or n').lower()
ontime = 'y'
# ontime = 'n'

# days_rented = int(input('How many days was the video rented?'))
days_rented = int('4')

# day_rented = input('What day was the video rented?').capitalize()
day_rented = 'sunday'.capitalize()
# day_rented = 'thursday'.capitalize()
# day_rented = 'monday'.capitalize()

cost_per_day = 1.59

if ontime == 'n':
    days_rented += 1
if day_rented == 'Sunday':
    total = (days_rented * cost_per_day) * .7
elif day_rented == 'Thursday':
    total = (days_rented * cost_per_day) * .5
else:
    total = (days_rented * cost_per_day)

print('Cost of the DVD rental is: $', total)
# n, 4, monday -> 7.95
# y, 4, monday -> 6.36
# y, 4, thursday -> 3.18
# y, 4, sunday -> 4.452
