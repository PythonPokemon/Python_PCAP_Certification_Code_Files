"""
Strings als Sequenzen: Indizierung
------------------------------------------------------------------------------------------------------------------------
Wir haben dir schon gesagt, dass Python-Strings Sequenzen sind. Es ist Zeit, dir zu zeigen, was das eigentlich bedeutet.

Strings sind keine Listen, aber man kann sie in vielen speziellen Fällen auch wie Listen behandeln.

Wenn du zum Beispiel auf einen Zeichenzug einer Zeichenkette zugreifen möchtest, 
kannst du das mit Indexierung tun, genau wie im untenstehenden Beispiel. Führen Sie das Programm aus:

------------------------------------------------------------------------------------------------------------------------
"""

# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()





"""
Strings als Sequenzen: Iteration
------------------------------------------------------------------------------------------------------------------------
Auch durch die Streicher zu iterieren. Schauen Sie sich das untenstehende Beispiel an:

------------------------------------------------------------------------------------------------------------------------
"""

# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()

