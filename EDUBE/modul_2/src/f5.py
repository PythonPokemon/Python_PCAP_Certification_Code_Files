"""
Operationen auf Zeichenketten: chr()
Wenn du den Codepunkt (Zahl) kennst und das entsprechende Zeichen erhalten möchtest, kannst du eine Funktion namens verwenden.chr()

Die Funktion nimmt einen Codepunkt und gibt dessen Zeichen zurück.

Das Aufrufen mit einem ungültigen Argument (z. B. einem negativen oder ungültigen Codepunkt) verursacht ValueError- oder TypeError-Ausnahmen.

Führe den Code im Editor aus. Das Beispiel-Snippet-Ergebnis:

a
α
Ausgabe

Anmerkung:

chr(ord(x)) == x
ord(chr(x)) == x
Führe deine eigenen Experimente durch.
"""
# Demonstrating the chr() function.

print(chr(97))
print(chr(945))
