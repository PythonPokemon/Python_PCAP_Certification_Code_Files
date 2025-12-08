"""

Operationen auf Saiten: ord()
Wenn du den ASCII/UNICODE-Codepunktwert eines bestimmten Zeichens wissen möchtest, kannst du eine Funktion namens (also Ordinal) verwenden.ord()

Die Funktion benötigt eine einstellige Zeichenkette als Argument – ein Bruch dieser Anforderung führt zu einer TypeError-Ausnahme und gibt eine Zahl zurück, die den Codepunkt des Arguments repräsentiert.

Schau dir den Code im Editor an und führe ihn aus. Der Ausschnitt liefert:

97
32
Ausgabe

Nun weisen Sie verschiedenen Werten und , z. B. (griechischer Alpha) und (ein Buchstaben im polnischen Alphabet); Dann führe den Code aus und schau, welches Ergebnis er liefert. Führe deine eigenen Experimente durch.char_1char_2αę



"""

# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))
