"""
Der Stack – objektorientierter Ansatz: Fortsetzung
Jetzt wollen wir die interne Stack-Liste vor externem Zugriff verbergen.

Dazu verwendet Python eine einfache, aber wirkungsvolle Konvention:
Wenn ein Attribut mit zwei Unterstrichen beginnt (__), wird es „privat“.

Beispiel:
    self.__stapel_liste

Effekt:
• Das Attribut ist NUR innerhalb der Klasse sichtbar.
• Von außen kann man NICHT darauf zugreifen.
• Dies wird als Kapselung (Encapsulation) bezeichnet.
• Python löst einen AttributeError aus, wenn man versucht,
  das Attribut von außen anzusprechen.

Das folgende Programm demonstriert diesen Schutzmechanismus:
"""
class Stapel:
    def __init__(self):
        self.__stapel_liste = []   # private Liste, nur intern zugänglich | weil 2 unterstriche __


stapel_objekt = Stapel()

# Dieser Zugriff von außen ist NICHT erlaubt:
print(len(stapel_objekt.__stapel_liste))   # → AttributeError
