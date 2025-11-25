
# start = input('How old were you at the time of joining?')
# now = input('How old are you today?')
start, now = '20', '65'  # Just for convenience

# You cannot subtract one string from another:
# print('Congrats on ' + str(now - start) + ' Years of Service!')
# TypeError
# print('Congrats on ' + int(now - start) + ' Years of Service!')
# TypeError

"""
# You cannot concatenate a string and an integer
print(
    'Congrats on '
    + (int(now) - int(start))
    + ' Years of Service!'
) # TypeError
"""

# This is the right way to do it:
print(
    'Congrats on '
    + str(int(now) - int(start))
    + ' Years of Service!'
)
# Congrats on 45 years of service!
