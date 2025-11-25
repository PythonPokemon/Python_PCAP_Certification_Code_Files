
def get_rating(age):
    rating = ''
    if age == None: rating = 'C'
    elif age < 13: rating = 'C'
    elif age < 18: rating = 'T'
    else: rating = 'A'
    return rating


print(get_rating(19))    # A
print(get_rating(18))    # A
print(get_rating(17))    # T
print(get_rating(13))    # T
print(get_rating(12))    # C
print(get_rating(11))    # C
print(get_rating(None))  # C
