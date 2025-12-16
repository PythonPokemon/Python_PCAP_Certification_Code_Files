"""
Generatoren – wo man sie findet (Fortsetzung)
Das Iterator-Protokoll verstehen (Edube / PCAP-relevant)

-----------------------------------------------------------
Was ist ein Iterator?
-----------------------------------------------------------
Ein Iterator ist ein Objekt, das zwei Methoden besitzen MUSS:

1) __iter__()
   • wird EINMAL zu Beginn aufgerufen
   • muss den Iterator selbst zurückgeben

2) __next__()
   • liefert bei jedem Aufruf den NÄCHSTEN Wert der Sequenz
   • wenn keine Werte mehr existieren → StopIteration auslösen

Nur wenn beide Methoden vorhanden sind, kann ein Objekt in einer
for-Schleife oder in einer in-Abfrage verwendet werden.

-----------------------------------------------------------
Warum braucht Python dieses Protokoll?
-----------------------------------------------------------
for i in irgendwas:
    …

Python fragt intern:
1. „Hast du eine __iter__()-Methode?“ → Iterator abrufen
2. „Hast du eine __next__()-Methode?“ → nächsten Wert holen
3. Beim Ende der Daten → StopIteration → Schleife beendet

-----------------------------------------------------------
Beispiel aus der Aufgabe: Eigener Fibonacci-Iterator
-----------------------------------------------------------
Der Iterator Fib(nn) soll die ersten nn Fibonacci-Zahlen liefern.
Definition:
    Fib1 = 1
    Fib2 = 1
    Fibi = Fibi-1 + Fibi-2

-----------------------------------------------------------
Ablauf im Code:
-----------------------------------------------------------
__init__():   richtet Startwerte ein
__iter__():   gibt sich selbst zurück (Iterator = Objekt)
__next__():   berechnet jede Fibonacci-Zahl und liefert sie

Wichtig:
• Wenn die gewünschte Anzahl erreicht ist → StopIteration
• Ohne StopIteration würde die Schleife unendlich laufen

-----------------------------------------------------------
Was zeigt die Ausgabe?
-----------------------------------------------------------
• __init__ wird 1× aufgerufen → Objekt wird erzeugt
• __iter__ wird 1× aufgerufen → for-Schleife startet
• __next__ wird 11× aufgerufen → 10 Werte + 1× StopIteration

Das ist exakt das Verhalten des Iterator-Protokolls.

-----------------------------------------------------------
Code (unverändert, nur kommentiert)
-----------------------------------------------------------
"""

class Fib:
    def __init__(self, nn):
        print("__init__")                         # wird beim Erzeugen eines Objekts ausgeführt
        self.__n = nn                             # Anzahl der gewünschten Fibonacci-Zahlen
        self.__i = 0                              # Zähler der bereits erzeugten Werte
        self.__p1 = self.__p2 = 1                 # Startwerte für F1 und F2

    def __iter__(self):
        print("__iter__")                         # for-Schleife ruft dies EINMAL auf
        return self                                # Iterator ist das Objekt selbst

    def __next__(self):
        print("__next__")                         # jeder Schleifendurchlauf ruft __next__() auf
        self.__i += 1
        if self.__i > self.__n:                    # Ende erreicht?
            raise StopIteration                    # → beendet die Iteration

        if self.__i in (1, 2):                     # F1 und F2 sind 1
            return 1

        ret = self.__p1 + self.__p2               # Fibonacci-Formel
        self.__p1, self.__p2 = self.__p2, ret     # Werte verschieben
        return ret                                 # nächste Zahl liefern


for i in Fib(10):                                 # Iterator über die ersten 10 Fibonacci-Zahlen
    print(i)                                      # Ausgabe der einzelnen Werte
