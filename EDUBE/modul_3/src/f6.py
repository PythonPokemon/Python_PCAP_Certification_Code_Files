"""
Der Objekt-Ansatz: ein Stapel von Grund auf – Fortsetzung

Ein großer Vorteil der objektorientierten Programmierung:
Man kann beliebig viele Objekte derselben Klasse erzeugen.
Jedes Objekt besitzt seine EIGENEN privaten Daten,
aber alle teilen sich denselben Satz an Methoden.

Beim Stack bedeutet das:
• Jeder Stapel hat seine eigene private Liste __stapel_liste
• Jeder Stapel verhält sich gleich (push, pop)
• Stapel beeinflussen sich NICHT gegenseitig

Im Beispiel unten erzeugen wir zwei getrennte Stapel:
    stapel_1 = Stapel()
    stapel_2 = Stapel()

Ablauf:
1) stapel_1.push(3) legt eine 3 auf den ersten Stapel.
2) stapel_2.push(stapel_1.pop()) nimmt das oberste Element aus stapel_1
   und legt es oben auf stapel_2.
3) print(stapel_2.pop()) entnimmt den Wert aus stapel_2 und gibt ihn aus.

Erwartete Ausgabe:
    3

Dadurch wird gezeigt:
• Beide Stack-Objekte sind unabhängig.
• Die privaten Daten gehören immer dem jeweiligen Objekt.
• Methoden funktionieren für alle Objekte gleichermaßen.
"""
class Stapel:
    def __init__(self):
        self.__stapel_liste = []   # private Liste für jeden Stapel

    def push(self, wert):
        self.__stapel_liste.append(wert)

    def pop(self):
        oberster_wert = self.__stapel_liste[-1]
        del self.__stapel_liste[-1]
        return oberster_wert


# Zwei unabhängige Stapel-Objekte erstellen
stapel_1 = Stapel()
stapel_2 = Stapel()

# Werte verschieben
stapel_1.push(3)
stapel_2.push(stapel_1.pop())

# Ausgabe
print(stapel_2.pop())   # → 3
