"""
Python-Strings sind unveränderlich
-------------------------------------------------------------------------------------------------------------------------------
Wir haben Ihnen auch gesagt, dass die Python-Strings unveränderlich sind. Das ist ein sehr wichtiges Merkmal. Was bedeutet das?

Das bedeutet hauptsächlich, dass die Ähnlichkeit von Strings und Listen begrenzt ist. 
Nicht alles, was man mit einer Liste machen kann, kann mit einer Schnur gemacht werden.

Der erste wichtige Unterschied erlaubt es nicht, die Del-Instruktion zu verwenden, um irgendetwas von einer Zeichenkette zu entfernen.
"""

# Das Beispiel hier funktioniert nicht:
alphabet = "abcdefghijklmnopqrstuvwxyz"
del alphabet[0]

# Das Einzige, was du mit einer Schnur machen kannst, ist, die Schnur als Ganzes zu entfernen. Versuch es.del
#del alphabet       # probier es aus!
#print(alphabet)    # probier es aus!

"""
Python-Strings haben keine append()-Methode – du kannst sie in keiner Weise erweitern.
"""
# Das folgende Beispiel ist fehlerhaft:
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.append("A")

# Ohne die Methode ist die Insert()-Methode ebenfalls illegal:append()
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.insert(0, "A")