"""
Lambdas und die map()-Funktion
Funktionen auf Sequenzen anwenden (Iteratoren)

-----------------------------------------------------------
Was ist die Idee hinter map()?
-----------------------------------------------------------
map() wendet eine Funktion auf JEDES Element
einer Sequenz (Iterable) an und liefert die
Ergebnisse als Iterator zurück.

Grundform:
    map(funktion, iterable)

Wichtig:
• map() liefert KEINE Liste, sondern einen Iterator
• das Iterable kann sein:
  - Liste
  - Tupel
  - Generator
• das Ergebnis muss meist:
  - mit list() umgewandelt ODER
  - direkt mit for verarbeitet werden

-----------------------------------------------------------
Warum Lambdas hier ideal sind
-----------------------------------------------------------
Die übergebene Funktion ist:
• sehr kurz
• nur einmal notwendig
• mathematisch einfach

→ perfekte Einsatzstelle für lambda

Syntax:
    lambda parameter: ausdruck

Der Ausdruck ist automatisch der Rückgabewert.

-----------------------------------------------------------
Beispiel aus der Aufgabe
-----------------------------------------------------------
Ziel:
1) Liste mit Zahlen 0–4 erzeugen
2) daraus Zweierpotenzen berechnen
3) anschließend jedes Ergebnis quadrieren
"""

# Schritt 1: Basisliste erzeugen
liste_1 = [zahl for zahl in range(5)]                  # [0, 1, 2, 3, 4]

# Schritt 2: Zweierpotenzen berechnen (Iterator → Liste)
liste_2 = list(map(lambda zahl: 2 ** zahl, liste_1))
print(liste_2)                                         # Ausgabe: [1, 2, 4, 8, 16]

# Schritt 3: map()-Iterator direkt verwenden (ohne list)
for wert in map(lambda wert: wert * wert, liste_2):
    print(wert, end=" ")
print()                                                 # Ausgabe: 1 4 16 64 256



"""
-----------------------------------------------------------
Was passiert hier?
-----------------------------------------------------------
• Erste map():
  lambda zahl: 2 ** zahl
  → berechnet für jedes Element die Zweierpotenz
  → list() macht daraus eine echte Liste

• Zweite map():
  lambda wert: wert * wert
  → quadriert jedes Element
  → KEINE Liste, Werte werden direkt erzeugt

• for-Schleife verbraucht den Iterator sofort

-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• map() gibt IMMER einen Iterator zurück
• print(map(...)) zeigt nur:
  <map object at 0x...>
• Um Werte zu sehen:
  - for wert in map(...)
  - oder list(map(...))
• Iteratoren sind EINMAL verwendbar

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• Nach einmaligem Durchlaufen ist der map()-Iterator leer
• lambda darf:
  - NUR einen Ausdruck enthalten
  - KEINE Schleifen, KEIN return, KEINE Blöcke
• lambda x: print(x) → gültig, Rückgabewert ist None

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
map() + lambda ist ideal für:
• kurze Berechnungen
• Einmal-Transformationen
• speichersparendes Arbeiten mit Iteratoren
"""
