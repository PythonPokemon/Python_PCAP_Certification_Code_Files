
# day = input('Enter the day of the week:')
day = 'Friday'       # Just for convenience
# day = 'Wednesday'  # 8
# day = 'Thursday'   # 10
# day = 'Saturday'   # 13
# day = 'Sunday'.    # 23
discount = 3

if day == 'Wednesday':
    discount += 5
elif day == 'Thursday':
    discount += 7
elif day == 'Saturday':
    discount += 10
elif day == 'Sunday':
    discount += 20
else:
    discount += 2

print(discount)  # 5
