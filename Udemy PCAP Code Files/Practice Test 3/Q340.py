
# First execute the following to create a file
# with already existing players:
players = '''Peter
Paul
Mary
Jane
'''
with open('players.txt', 'w') as f:
    f.write(players)

player = 'Steve'
with open('players.txt', 'a+') as f:
    f.write(player)
    f.seek(0)
    # f.flush()  # -> no error, but also no output
    # f.begin()  # AttributeError: ...
    # f.close()  # In the next line: ValueError: ...
    data = f.read()
    print(data)

"""
Peter
Paul
Mary
Jane
Steve
"""
