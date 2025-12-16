"""
Generatoren – wo man sie findet
Einführung in Generatoren, Iteratoren & das Iterationsprotokoll

-----------------------------------------------------------
Was ist ein Generator?
-----------------------------------------------------------
Ein Generator ist ein spezieller Code, der:
• eine FOLGE von Werten liefert (nicht nur einen wie eine Funktion)
• seinen Zustand zwischen den einzelnen Lieferungen speichert
• den Iterationsprozess selbst steuert

Generatoren werden daher häufig mit Iteratoren gleichgesetzt.

-----------------------------------------------------------
Wo begegnen dir Generatoren schon jetzt?
-----------------------------------------------------------
Beispiel:
    for i in range(5):
        print(i)

Die Funktion range() IST ein Generator (genauer: liefert ein Iterator-Objekt).

Warum?
• range(5) erzeugt keine Liste → es erzeugt ein Objekt, das
  nacheinander Werte zurückgibt
• Bei jedem Schleifendurchlauf fragt Python: „Hast du den nächsten Wert?“
• range liefert: 0, 1, 2, 3, 4 → und STOP → dann endet die for-Schleife

-----------------------------------------------------------
Generator vs. Funktion
-----------------------------------------------------------
Funktion:
• liefert EIN Ergebnis
• wird EINMAL ausgeführt

Generator:
• liefert MEHRERE Ergebnisse nacheinander
• wird IMMER WIEDER aufgerufen, bis keine Werte mehr existieren

-----------------------------------------------------------
Wie oft wird ein Generator aufgerufen?
-----------------------------------------------------------
Im Beispiel:
    for i in range(5):
        print(i)

range(5) wird intern SECHSMAL abgefragt:
• fünfmal → liefert Werte 0 bis 4
• sechstes Mal → meldet: „Kein Wert mehr“ (StopIteration)

-----------------------------------------------------------
Warum ist das transparent?
-----------------------------------------------------------
Python versteckt internes Verhalten:
• Die Schleife ruft still und heimlich den Iterator ab
• Die Schleife ruft still und heimlich „next()“ auf
• Der Entwickler bekommt nur sauberes Verhalten zu sehen

Wir schauen uns als Nächstes das sogenannte ITERATOR-PROTOKOLL an.
Das erklärt exakt, wie ein Generator intern funktioniert.

-----------------------------------------------------------
Codebeispiel aus der Aufgabe
-----------------------------------------------------------
"""

for i in range(5):                  # range erzeugt einen Generator / Iterator
    print(i)                        # Ausgabe der Werte 0 bis 4
