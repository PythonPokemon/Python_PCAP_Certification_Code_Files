"""
Generatoren – eigene Generatoren mit yield bauen
Potenzen, Listen, Mitgliedschaft, Fibonacci (EDUBE/PCAP)

-----------------------------------------------------------
Warum eigene Generatoren?
-----------------------------------------------------------
Generatoren erzeugen Werte SCHRITTWEISE statt alles auf einmal.
Vorteile:
• weniger Speicherverbrauch
• einfachere Logik als __iter__/__next__
• Zustand wird automatisch gespeichert

-----------------------------------------------------------
Beispiel 1:
Generator für Potenzen von 2
-----------------------------------------------------------
Erzeugt die ersten n Potenzen von 2.
"""

def potenzen_von_2(n):
    wert = 1
    for i in range(n):
        yield wert            # aktuellen Wert zurückgeben → pausieren
        wert *= 2            # nächsten Wert vorbereiten

for v in potenzen_von_2(8):
    print(v)                 # Ausgabe: 1 2 4 8 16 32 64 128


# bsp. 2
print()
"""
-----------------------------------------------------------
Generatoren in Listenverständnissen
-----------------------------------------------------------
Ein Generator kann direkt in einer Liste gesammelt werden.
"""

def potenzen_von_2(n):
    wert = 1
    for i in range(n):
        yield wert
        wert *= 2

liste = [x for x in potenzen_von_2(5)]
print(liste)                 # Ausgabe: [1, 2, 4, 8, 16]


# bsp. 3
print()
"""
-----------------------------------------------------------
list() – Generator in Liste umwandeln
-----------------------------------------------------------
list(generator) zwingt den Generator,
ALLE Werte sofort zu erzeugen.
"""

def potenzen_von_2(n):
    wert = 1
    for i in range(n):
        yield wert
        wert *= 2

liste = list(potenzen_von_2(3))
print(liste)                 # Ausgabe: [1, 2, 4]



# bsp. 4
print()
"""
-----------------------------------------------------------
Der in-Operator mit Generatoren
-----------------------------------------------------------
Achtung (sehr prüfungsrelevant):
'X in generator' startet den Generator jedes Mal NEU!
Er durchsucht die erzeugte Sequenz.
"""

def potenzen_von_2(n):
    wert = 1
    for i in range(n):
        yield wert
        wert *= 2

for i in range(20):
    if i in potenzen_von_2(4):   # prüft 1, 2, 4, 8
        print(i)
# Ausgabe: 1 2 4 8


# bsp. 5
print()
"""
-----------------------------------------------------------
Fibonacci-Generator (vereinfachte Version)
-----------------------------------------------------------
Erzeugt die ersten n Fibonacci-Zahlen.
Viel kürzer als die Iterator-Klassenversion.
"""

def fibonacci(n):
    a = b = 1
    for i in range(n):
        if i < 2:
            yield 1
        else:
            neu = a + b
            a, b = b, neu
            yield neu

folge = list(fibonacci(10))
print(folge)    # Ausgabe: [1,1,2,3,5,8,13,21,34,55]
