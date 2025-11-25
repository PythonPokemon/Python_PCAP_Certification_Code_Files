
# room = input('Enter the room number: ')
room = '101'  # Just for convenience
rooms = {101: 'Gathering Place', 102: 'Meeting Room'}
if not room in rooms:
    # if room not in rooms:
    print('The room does not exist.')
else:
    print('The room name is: ' + rooms[room])

d = {'101': "String", 101: "Integer"}

"""
Hi Paidrigin,
that's a good question, because in other languages this would be a syntax error.
In Python
if not room in rooms:
is "only" a violation against the Python coding conventions
(In this case PEP8 E713).
It should read:
if room not in rooms:
But both work.
Look also here:
https://stackoverflow.com/questions/17659303/what-is-more-pythonic-for-not
I hope that clears it up. Otherwise, please get back to me.
With kind regards,
Cord
"""


