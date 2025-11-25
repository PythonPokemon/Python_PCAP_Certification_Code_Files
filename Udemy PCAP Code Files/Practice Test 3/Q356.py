
def get_name():
    # name = input('What is your name? ')
    name = 'Peter'
    return name


def calc_calories(miles, calories_per_mile):
    calories = miles * calories_per_mile
    return calories


# distance = int(input('How many miles did you bike this week? '))
distance = int('740')
burn_rate = 50
biker = get_name()
calories_burned = calc_calories(distance, burn_rate)
print(biker + ', you burned about', calories_burned, 'calories.')
# Peter, you burned about 37000 calories.
