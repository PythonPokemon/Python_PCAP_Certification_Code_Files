"""
Die lstrip()-Methode
Die parameterlose Methode gibt eine neu erstellte Zeichenkette zurück, die aus dem ursprünglichen gebildet wurde, 
indem alle führenden bzs. Leerräume die am anfang, also vor dem string tau stehen entfernt werden.lstrip()

Analysiere den Beispielcode im Editor.

Die Klammern sind kein Teil des Ergebnisses – sie zeigen nur die Grenzen des Ergebnisses.
"""

# Demonstrating the lstrip() method:
print("[" + " __tau ".lstrip() + "]")





"""
Die Ein-Parameter-Methode macht dasselbe wie ihre parameterlose Version, 
entfernt jedoch alle in ihrem Argument (einer Zeichenkette) aufgeführten Zeichen, nicht nur Leerzeichen
"""

# bsp. 2 mit parameter, der den 'anfang' des strings entfernen soll
print("www.cisco.com".lstrip("w."))

# bsp. 3 mit parameter der das 'ende' des strings entfernen soll
print("pythoninstitute.org".lstrip(".org"))

