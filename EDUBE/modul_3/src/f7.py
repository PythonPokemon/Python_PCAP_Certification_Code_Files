"""
Der Objektansatz: ein Stapel von Grund auf (Fortsetzung)

In diesem Beispiel haben wir drei unabhängige Stack-Objekte:

    little_stack
    another_stack
    funny_stack

Alle besitzen ihre eigene private Liste __stapel_liste.

Wir analysieren den Ablauf SCHRITT FÜR SCHRITT:

---------------------------------------------------------
1) little_stack.push(1)
---------------------------------------------------------
little_stack = [1]

---------------------------------------------------------
2) another_stack.push(little_stack.pop() + 1)
---------------------------------------------------------
• little_stack.pop() liefert 1 und entfernt das Element:
      little_stack = []
• 1 + 1 = 2
• another_stack.push(2) → another_stack = [2]

---------------------------------------------------------
3) funny_stack.push(another_stack.pop() - 2)
---------------------------------------------------------
• another_stack.pop() liefert 2 und entfernt es:
      another_stack = []
• 2 - 2 = 0
• funny_stack.push(0) → funny_stack = [0]

---------------------------------------------------------
4) print(funny_stack.pop())
---------------------------------------------------------
• funny_stack.pop() liefert 0 und entfernt es
• Ausgabe: 0

Der erwartete Bildschirmwert lautet also:
    0
"""
class Stapel:
    def __init__(self):
        self.__stapel_liste = []

    def push(self, wert):
        self.__stapel_liste.append(wert)

    def pop(self):
        oberster_wert = self.__stapel_liste[-1]
        del self.__stapel_liste[-1]
        return oberster_wert


# Drei unabhängige Stapel erzeugen
kleiner_stapel = Stapel()
anderer_stapel = Stapel()
lustiger_stapel = Stapel()

kleiner_stapel.push(1)
anderer_stapel.push(kleiner_stapel.pop() + 1)   # 1 + 1 = 2
lustiger_stapel.push(anderer_stapel.pop() - 2)  # 2 - 2 = 0

print(lustiger_stapel.pop())   # → 0
