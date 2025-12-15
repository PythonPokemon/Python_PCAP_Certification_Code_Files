"""
Das Diamond-Problem (Mehrfachvererbung)

Beim „Diamond-Problem“ sieht die Vererbung wie ein Diamant aus:

        A
       / \
      B   C
       \ /
        D

- A ist die Oberklasse (Top).
- B und C erben beide von A.
- D erbt von B und C (Reihenfolge ist wichtig!).

Das Problem entsteht, wenn B und C dieselbe Methode/Variable bereitstellen:
Welche Version soll D verwenden?

Python löst das über die MRO (Method Resolution Order):
Python sucht Attribute/Methoden in einer festen Reihenfolge und nimmt die erste passende.

Merksatz (PCAP):
- Bei D(B, C) wird zuerst in D gesucht, dann in B, dann in C, dann in A.
- Bei D(C, B) wird zuerst in D gesucht, dann in C, dann in B, dann in A.

Wir schauen uns das mit print() an:
- __mro__ zeigt die Suchreihenfolge (MRO) an.
- m_middle() ist in B und C definiert -> Python nimmt die erste Klasse aus der MRO, die m_middle() hat.
"""

class KlasseA:
    def m_top(self):
        print("top")                                  # Methode aus der Oberklasse A

class KlasseB(KlasseA):
    def m_middle(self):
        print("middle_left")                          # „linke“ Middle-Methode (B)

class KlasseC(KlasseA):
    def m_middle(self):
        print("middle_right")                         # „rechte“ Middle-Methode (C)

class KlasseD(KlasseB, KlasseC):
    def m_bottom(self):
        print("bottom")                               # Methode aus D


objekt = KlasseD()

print(KlasseD.__mro__)                                # MRO: zeigt Suchreihenfolge der Klassen
objekt.m_bottom()                                     # bottom (aus D)
objekt.m_middle()                                     # middle_left (aus B, weil B vor C steht)
objekt.m_top()                                        # top (aus A)
