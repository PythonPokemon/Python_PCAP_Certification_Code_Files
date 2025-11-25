
# order = int(input('Please enter the order value: '))
# state = input('Please enter the state (as postal abbreviation): ')
order, state = int('1700'), 'FL'  # Just for convenience
delivery = 0

if state in ['NC', 'SC', 'VA']:
    if order <= 1000:
        delivery = 70
    elif 1000 < order < 2000:
        delivery = 80
    else:
        delivery = 90
else:
    delivery = 50
    print('1. delivery', delivery)      # 50
if state in ['GA', 'WV', 'FL']:
    if order > 1000:
        delivery += 30
        print('2. delivery', delivery)  # 80
    if order < 2000 and state in ['WV', 'FL']:
        delivery += 40
        print('3. delivery', delivery)  # 120
    else:
        delivery += 25
print(delivery)  # 120
