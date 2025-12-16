"""
Lambdas und die filter()-Funktion
Sequenzen gezielt filtern mit Bedingungen

-----------------------------------------------------------
Was ist die Idee hinter filter()?
-----------------------------------------------------------
filter() entfernt Elemente aus einer Sequenz anhand
einer Bedingung.

Grundform:
    filter(funktion, iterable)

• funktion muss True oder False zurückgeben
• NUR Elemente mit True bleiben erhalten
• Ergebnis ist ein Iterator (keine Liste!)

-----------------------------------------------------------
Warum Lambdas hier ideal sind
-----------------------------------------------------------
Die Filter-Bedingung ist meist:
• sehr kurz
• logisch (Vergleich / Bedingung)
• nur einmal nötig

→ perfekte Einsatzstelle für lambda

Syntax:
    lambda parameter: bedingung

Die Bedingung liefert True oder False zurück.

-----------------------------------------------------------
Beispiel aus der Aufgabe
-----------------------------------------------------------
Ziel:
1) Zufällige Zahlen zwischen -10 und +10 erzeugen
2) Nur Zahlen behalten, die:
   • größer als 0 sind
   • UND gerade sind
"""

from random import seed, randint

seed()                                                  # Zufallszahlengenerator initialisieren

# Schritt 1: Zufällige Liste erzeugen
daten = [randint(-10, 10) for _ in range(5)]
print(daten)                                            # z. B.: [6, 3, 3, 2, -7]

# Schritt 2: Liste filtern (Iterator → Liste)
gefiltert = list(
    filter(
        lambda zahl: zahl > 0 and zahl % 2 == 0,        # Bedingung: positiv UND gerade
        daten
    )
)

print(gefiltert)                                        # z. B.: [6, 2]



"""
-----------------------------------------------------------
Was passiert hier?
-----------------------------------------------------------
• lambda zahl: zahl > 0 and zahl % 2 == 0
  → liefert True nur für:
    - positive Zahlen
    - gerade Zahlen

• filter() ruft das Lambda für JEDES Element auf
• Nur True-Ergebnisse bleiben erhalten
• list() macht aus dem Iterator eine echte Liste

-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• filter() gibt IMMER einen Iterator zurück
• Ohne list() sieht man nur:
  <filter object at 0x...>
• Die Filter-Funktion MUSS True/False liefern
• Iteratoren sind EINMAL nutzbar

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
lambda x: x % 2
→ funktioniert, weil:
  - 0 = False
  - 1 = True
ABER: schlechter Stil, unklar!

Besser:
lambda x: x % 2 == 0

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
filter() + lambda ist ideal für:
• Auswahllogik
• Bedingungen
• sauberes, lesbares Filtern von Sequenzen
"""
