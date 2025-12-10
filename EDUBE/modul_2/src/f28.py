"""
Die rstrip()-Methode
Zwei Varianten der Methode bewirken nahezu dasselbe wie s, beeinflussen jedoch die gegenüberliegende Seite der Zeichenkette.
rstrip()
lstrip
"""

# Demonstrating the rstrip() method:
print("[" + " upsilon ".rstrip() + "]")     # entfernt das leerzeichen vorkommen beginnent von 'rechts'
print("cisco.com".rstrip(".com"))


# Demonstrating the lstrip() method:
print("[" + " upsilon ".lstrip() + "]")     # entfernt das leerzeichen vorkommen beginnent von 'links'
print("cisco.com".lstrip("cisco"))


"""

"""

