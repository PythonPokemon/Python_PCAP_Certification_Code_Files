"""
Die Methode capitalize()
Gehen wir einige Standard-Python-String-Methoden durch. Wir werden sie in alphabetischer Reihenfolge durchgehen – ehrlich gesagt hat jede Reihenfolge ebenso viele Nachteile wie Vorteile, daher kann die Wahl genauso gut zufällig sein.

Die Methode tut genau das, was sie verspricht – sie erstellt einen neuen String, der mit Zeichen aus dem Quellstring gefüllt ist, versucht aber, diese folgendermaßen zu modifizieren:capitalize()

Wenn das erste Zeichen innerhalb der Zeichenkette ein Buchstabe ist (Hinweis: Das erste Zeichen ist ein Element mit einem Index gleich 0, nicht nur das erste sichtbare Zeichen), wird es in Großbuchstaben umgewandelt;
alle verbleibenden Buchstaben der Zeichenkette werden in Kleinbuchstaben umgewandelt.
Vergiss nicht, dass:

Die ursprüngliche Zeichenkette (von der aus die Methode aufgerufen wird) wird in keiner Weise verändert (die Unveränderlichkeit einer Zeichenkette muss ohne Vorbehalt beachtet werden)
Die modifizierte (in diesem Fall großgeschriebene) Zeichenkette wird als Ergebnis zurückgegeben – wenn du sie in keiner Weise verwendest (einer Variablen zuordnest oder an eine Funktion/Methode weitergibst), verschwindet sie ohne Spur.
Hinweis: Methoden müssen nicht nur innerhalb von Variablen aufgerufen werden. Sie können direkt innerhalb von String-Literals aufgerufen werden. Wir werden diese Konvention regelmäßig verwenden – sie wird die Beispiele vereinfachen, da die wichtigsten Aspekte bei unnötigen Aufgaben nicht verschwinden.

"""

# Demonstrating the capitalize() method:
print('aBcD'.capitalize())
