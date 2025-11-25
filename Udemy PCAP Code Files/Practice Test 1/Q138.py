
import re
pattern = r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$'
email = 'peter.wellert@example.org'       # Valid!
# email = 'peter.wellert(at)example.org'  # Not valid!
if re.match(pattern, email):
    print('Valid!')
else:
    print('Not valid!')
